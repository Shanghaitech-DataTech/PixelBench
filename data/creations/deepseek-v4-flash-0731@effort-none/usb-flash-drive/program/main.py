from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="usb")

# Design: USB flash drive item portrait, pointing right.
# Keychain split ring at far left, metal casing body in the middle,
# USB connector at far right. Transparent background.

outline = c.color('#16130f')
m_hi = c.color('#f5f5f5')
m_lt = c.color('#dcdcdc')
m_md = c.color('#b9b9b9')
m_dk = c.color('#909090')
m_drk = c.color('#646464')
m_deep = c.color('#444444')
u_lt = c.color('#e6e6e6')
u_md = c.color('#a3a3a3')
r_dk = c.color('#8d1f1f')
r_md = c.color('#ad2f2f')
r_lt = c.color('#d05a5a')

# --- 1. Keychain split ring (far left) ---
c.circle(6, 16, 4, r_md, fill=True)
c.circle(6, 16, 2, None, fill=True)
c.circle(6, 16, 4, outline, fill=False)
# Ring highlights (top-left)
c.circle(3, 14, 1, r_lt, fill=True)
c.set(4, 13, r_lt)
c.set(5, 12, r_lt)
c.set(6, 12, r_lt)
c.set(7, 13, r_lt)
# Ring shadows (bottom)
c.set(3, 18, r_dk)
c.set(4, 19, r_dk)
c.set(5, 20, r_dk)
c.set(6, 20, r_dk)

# --- 2. Connecting bracket (ring-to-body mount) ---
c.rect(6, 13, 6, 7, r_dk, fill=True)
c.rect(6, 13, 6, 7, outline, fill=False)
c.rect(7, 14, 4, 5, r_md, fill=True)

# --- 3. Main metal casing body ---
c.rect(11, 7, 16, 18, outline, fill=True)
c.rect(12, 8, 14, 16, m_md, fill=True)
c.rect(12, 8, 14, 3, m_hi, fill=True)
c.rect(12, 11, 14, 2, m_lt, fill=True)
c.rect(12, 19, 14, 5, m_dk, fill=True)
c.rect(12, 21, 14, 3, m_drk, fill=True)
c.rect(12, 23, 14, 1, m_deep, fill=True)

# Panel seam near connector end
c.rect(23, 8, 4, 16, m_drk, fill=True)
c.rect(24, 8, 3, 12, m_md, fill=True)
c.rect(23, 8, 1, 16, m_deep, fill=True)

# Screws
c.set(13, 9, outline)
c.set(24, 22, outline)
c.set(13, 22, m_deep)

# Raised brand label plate with etched text
c.rect(14, 13, 6, 5, m_lt, fill=True)
c.rect(14, 13, 6, 1, m_hi, fill=True)
c.rect(14, 13, 1, 5, m_hi, fill=True)
c.rect(19, 13, 1, 5, m_hi, fill=True)
c.rect(14, 17, 6, 1, m_dk, fill=True)
c.rect(15, 15, 4, 1, m_deep, fill=True)

# LED indicator
c.set(14, 20, r_lt)

# --- 4. USB connector (far right) ---
c.rect(27, 11, 4, 10, outline, fill=True)
c.rect(27, 12, 1, 8, u_lt, fill=True)
c.rect(28, 12, 2, 8, u_md, fill=True)
c.rect(28, 14, 2, 2, outline, fill=True)
c.rect(28, 18, 2, 2, outline, fill=True)

print(c.stats_text())

finish(c)
