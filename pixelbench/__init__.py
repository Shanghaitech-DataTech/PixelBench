"""PixelBench: an agentic pixel-art benchmark for GPT-style LLMs.

Core representation: a pixel art is
``palette + integer-id matrix + metadata``.  The artwork is delivered as a
program: agents edit Python source in a workspace and run it against the
drawing API, each run redrawing ``PixelCanvas`` objects from the task input in
a fresh process (:class:`pixelbench.repl.file_session.FileSession`).  The
legacy ipykernel session (:class:`pixelbench.repl.kernel.KernelSession`) is
kept for the standalone console and older integrations.
"""

from pixelbench._version import __version__
from pixelbench.core.canvas import ERASE, KEEP, PixelCanvas
from pixelbench.core.color import Color, Palette, parse_hex
from pixelbench.core.render import load_png_as_canvas, render_pil, render_png_bytes
from pixelbench.core.serialization import from_pixel_json, to_pixel_json
from pixelbench.repl.kernel import KernelSession

__all__ = [
    "__version__",
    "PixelCanvas",
    "KEEP",
    "ERASE",
    "Color",
    "Palette",
    "parse_hex",
    "render_pil",
    "render_png_bytes",
    "load_png_as_canvas",
    "to_pixel_json",
    "from_pixel_json",
    "KernelSession",
]
