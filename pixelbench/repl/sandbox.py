"""Confine an agent program before it runs (Linux, unprivileged, irreversible for the process).

Every program a model writes runs in a fresh process that is locked down before the first line of
model code executes. Without it, a program would run as ordinary host Python with access to the whole
file system (including the task's hidden evaluation files and other runs) and to the network.

* Landlock (ABI >= 1): the process may read and write only its own run directory (plus any extra
  writable paths), read the Python installation and the ``pixelbench`` package, and read system
  libraries. Everything else, including the rest of the repository, is denied. Nothing may be executed.
* seccomp: socket creation, exec, ptrace, process_vm_* and io_uring fail with EPERM.

``lock`` raises if Landlock or seccomp cannot be installed, so a run never silently goes unconfined.
"""
from __future__ import annotations

import ctypes
import os
import platform
import struct
import sys
from pathlib import Path

# ---------------------------------------------------------------- Landlock (ABI 1)
_SYS_CREATE_RULESET, _SYS_ADD_RULE, _SYS_RESTRICT_SELF = 444, 445, 446
_RULE_PATH_BENEATH = 1
EXECUTE, WRITE_FILE, READ_FILE, READ_DIR = 1 << 0, 1 << 1, 1 << 2, 1 << 3
_ALL_V1 = (1 << 13) - 1          # EXECUTE .. MAKE_SYM
_READ = READ_FILE | READ_DIR
_WRITE = _ALL_V1 & ~EXECUTE      # read, write, create and remove; never execute

_PR_SET_NO_NEW_PRIVS, _PR_SET_SECCOMP, _SECCOMP_MODE_FILTER = 38, 22, 2

_libc = ctypes.CDLL(None, use_errno=True)
_libc.syscall.restype = ctypes.c_long


def _err(what):
    e = ctypes.get_errno()
    return OSError(e, f'{what}: {os.strerror(e)}')


def landlock_abi() -> int:
    r = _libc.syscall(_SYS_CREATE_RULESET, None, ctypes.c_size_t(0), ctypes.c_uint32(1))
    return int(r) if r > 0 else 0


def _landlock(read_paths, write_paths):
    if landlock_abi() < 1:
        raise RuntimeError('Landlock is not available on this kernel; refusing to run unconfined')
    attr = struct.pack('=Q', _ALL_V1)
    fd = _libc.syscall(_SYS_CREATE_RULESET, ctypes.c_char_p(attr), ctypes.c_size_t(len(attr)), ctypes.c_uint32(0))
    if fd < 0:
        raise _err('landlock_create_ruleset')
    try:
        for paths, access in ((read_paths, _READ), (write_paths, _WRITE)):
            for p in paths:
                try:
                    pfd = os.open(p, os.O_PATH | os.O_CLOEXEC)
                except FileNotFoundError:
                    continue
                try:
                    rights = access if os.path.isdir(p) else access & (READ_FILE | WRITE_FILE)
                    rule = struct.pack('=Qi', rights, pfd)      # struct landlock_path_beneath_attr (packed)
                    if _libc.syscall(_SYS_ADD_RULE, ctypes.c_int(fd), ctypes.c_int(_RULE_PATH_BENEATH),
                                     ctypes.c_char_p(rule), ctypes.c_uint32(0)) < 0:
                        raise _err(f'landlock_add_rule {p}')
                finally:
                    os.close(pfd)
        if _libc.prctl(_PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) != 0:
            raise _err('prctl(NO_NEW_PRIVS)')
        if _libc.syscall(_SYS_RESTRICT_SELF, ctypes.c_int(fd), ctypes.c_uint32(0)) < 0:
            raise _err('landlock_restrict_self')
    finally:
        os.close(fd)


# ---------------------------------------------------------------- seccomp
_AUDIT_ARCH_X86_64 = 0xC000003E
_RET_ALLOW, _RET_EPERM, _RET_KILL = 0x7FFF0000, 0x00050001, 0x80000000
_DENY_X86_64 = {
    41: 'socket', 59: 'execve', 322: 'execveat', 101: 'ptrace',
    310: 'process_vm_readv', 311: 'process_vm_writev', 425: 'io_uring_setup',
}


class _SockFilter(ctypes.Structure):
    _fields_ = [('code', ctypes.c_ushort), ('jt', ctypes.c_ubyte), ('jf', ctypes.c_ubyte), ('k', ctypes.c_uint)]


class _SockFprog(ctypes.Structure):
    _fields_ = [('len', ctypes.c_ushort), ('filter', ctypes.POINTER(_SockFilter))]


def _seccomp():
    if platform.machine() != 'x86_64':
        raise RuntimeError(f'seccomp filter only written for x86_64, not {platform.machine()}')
    LD, JEQ, JGE, RET = 0x20, 0x15, 0x35, 0x06     # BPF_LD|W|ABS, BPF_JMP|JEQ|K, BPF_JMP|JGE|K, BPF_RET|K
    deny = sorted(_DENY_X86_64)
    prog = [(LD, 0, 0, 4),                                  # arch
            (JEQ, 1, 0, _AUDIT_ARCH_X86_64),
            (RET, 0, 0, _RET_KILL),                          # foreign ABI: kill
            (LD, 0, 0, 0),                                   # syscall number
            (JGE, len(deny) + 1, 0, 0x40000000)]             # x32 ABI -> deny
    for i, nr in enumerate(deny):
        prog.append((JEQ, len(deny) - i, 0, nr))             # match -> deny
    prog += [(RET, 0, 0, _RET_ALLOW), (RET, 0, 0, _RET_EPERM)]
    arr = (_SockFilter * len(prog))(*[_SockFilter(*x) for x in prog])
    fprog = _SockFprog(len(prog), arr)
    if _libc.prctl(_PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0) != 0:
        raise _err('prctl(NO_NEW_PRIVS)')
    if _libc.prctl(_PR_SET_SECCOMP, _SECCOMP_MODE_FILTER, ctypes.byref(fprog), 0, 0) != 0:
        raise _err('prctl(SECCOMP)')


# ---------------------------------------------------------------- policy
def _python_read_paths():
    out = {sys.prefix, sys.base_prefix, sys.exec_prefix, sys.base_exec_prefix}
    for p in sys.path:
        if p and ('site-packages' in p or 'dist-packages' in p or p.endswith('.zip') or 'lib-dynload' in p):
            out.add(p)
    return out


SYSTEM_READ = ['/usr/lib', '/usr/lib64', '/usr/lib32', '/lib', '/lib64', '/lib32', '/usr/share/zoneinfo',
               '/usr/share/fonts', '/etc/ld.so.cache', '/etc/localtime', '/dev/urandom', '/dev/random']
SYSTEM_WRITE = ['/dev/null']


def lock(run_dir, extra_write=(), extra_read=()):
    """Confine this process to ``run_dir``. Irreversible; call right before untrusted code runs."""
    import pixelbench
    package = Path(pixelbench.__file__).resolve().parent
    read = {os.path.realpath(p) for p in (*_python_read_paths(), str(package), *SYSTEM_READ, *extra_read)}
    write = {os.path.realpath(p) for p in (str(run_dir), *SYSTEM_WRITE, *extra_write)}
    _landlock(sorted(read), sorted(write))
    _seccomp()
    os.environ['PIXELBENCH_SANDBOX'] = 'landlock+seccomp'
