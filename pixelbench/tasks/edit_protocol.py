"""Edit canvas rules.

An edit output may be **any size the agent chooses**: there is no longer a
"at most twice the input per side" cap, so growing the canvas to make room for
the edit is a normal, allowed move.  What remains enforced is only a technical
crash guard (:data:`MAX_CANVAS_PIXELS`) and the same-geometry / same-scale rules
that live in :mod:`pixelbench.repl.submission`, because those describe the
animation rather than the agent's freedom.
"""
import operator

# A single canvas bigger than this cannot be rendered, serialised or displayed
# (and would OOM the episode), so dimensions are rejected before allocation.
# This is a crash guard, not a task limit, and it is deliberately not stated in
# any agent-facing prompt.  4096x4096 is far above every task in the bank.
MAX_CANVAS_PIXELS = 16_777_216


def validate_edit_size(width, height, input_width=None, input_height=None):
    """Check a canvas dimension is a usable positive integer pair.

    ``input_width`` / ``input_height`` are accepted (and ignored) so existing
    call sites that pass the input size keep working; the size of the input no
    longer constrains the output.
    """
    try:
        if isinstance(width, bool) or isinstance(height, bool):
            raise TypeError
        width, height = operator.index(width), operator.index(height)
    except TypeError:
        raise ValueError('Canvas width and height must be positive integers.') from None
    if width <= 0 or height <= 0:
        raise ValueError('Canvas width and height must be positive integers.')
    if width * height > MAX_CANVAS_PIXELS:
        raise ValueError(
            f'Canvas {width}x{height} is too large to render '
            f'({width * height} px; the technical maximum is {MAX_CANVAS_PIXELS} px). '
            'Register a smaller canvas.'
        )
    return width, height


def visible_box(width, height, opaque):
    """Half-open bounding box of the visible pixels of a ``w*h`` index grid.

    ``opaque(i)`` answers whether index ``i`` is non-transparent.  Returns
    ``(x0, y0, x1, y1)`` or ``None`` for a fully transparent canvas.
    """
    x0 = y0 = None
    x1 = y1 = -1
    for i in range(width * height):
        if not opaque(i):
            continue
        x, y = i % width, i // width
        x0 = x if x0 is None else min(x0, x)
        y0 = y if y0 is None else min(y0, y)
        x1 = max(x1, x)
        y1 = max(y1, y)
    if x0 is None or y0 is None:
        return None
    return (x0, y0, x1 + 1, y1 + 1)


# A later frame whose subject is this much bigger/smaller than frame 1 reads as
# a zoom instead of as motion.  Calibrated against real submissions: genuine
# sprite motion (a punch, a recoil, a bow being drawn) stays well inside it.
MAX_FRAME_SCALE_CHANGE = 1.35
# Below this the subject is a pixel or two wide and the ratio is meaningless.
MIN_SUBJECT_SIDE = 8


def sequence_errors(shapes, boxes):
    """Cross-frame problems for one multi-frame submission.

    ``shapes`` is each frame's ``(width, height)``; ``boxes`` is each frame's
    visible bounding box (``None`` when the frame is fully transparent).  Returns
    a list of human-readable errors — empty when the sequence is well formed.

    The rules describe the animation, not a size cap: an edit output may be any
    size, but all frames of one sequence must share one canvas geometry and keep
    the subject at a constant scale, otherwise the artwork jumps between frames.
    """
    errors = []
    if len(shapes) < 2:
        return errors
    if len(set(shapes)) > 1:
        listing = ", ".join(f"frame {i+1}={w}x{h}" for i, (w, h) in enumerate(shapes))
        errors.append(
            f'every frame of one sequence must use the same canvas size, got {listing}; '
            'register one canvas geometry and place all frames on it'
        )
    if any(b is None for b in boxes):
        return errors
    w0, h0 = boxes[0][2] - boxes[0][0], boxes[0][3] - boxes[0][1]
    if w0 <= 0 or h0 <= 0 or min(w0, h0) < MIN_SUBJECT_SIDE:
        return errors
    for i, b in enumerate(boxes[1:], start=1):
        w, h = b[2] - b[0], b[3] - b[1]
        ratio = max(w / w0, h / h0, w0 / max(w, 1), h0 / max(h, 1))
        if ratio > MAX_FRAME_SCALE_CHANGE:
            errors.append(
                f'frame {i+1} draws the subject at {w}x{h} px while frame 1 uses {w0}x{h0} px '
                f'({ratio:.2f}x scale change); keep the subject the same size in every frame and '
                'move or redraw only the parts that change'
            )
    return errors


def crop_edit_input(canvas):
    """Trim only fully transparent outer rows/columns; retain RGBA and holes.

    An entirely transparent input has no content bounds and is kept unchanged.
    The returned half-open box refers to the original input coordinates.
    """
    import numpy as np
    from pixelbench.core.canvas import PixelCanvas
    visible = np.zeros(canvas.matrix.shape, dtype=bool)
    for color in canvas.palette:
        if color.rgba[3] > 0:
            visible |= canvas.matrix == color.id
    ys, xs = np.nonzero(visible)
    if not len(xs):
        return canvas.copy(), (0, 0, canvas.width, canvas.height)
    x0, y0, x1, y1 = int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1
    out = PixelCanvas(x1-x0, y1-y0, palette=canvas.palette.copy(),
                      transparent_id=canvas.transparent_id,
                      initial=canvas.matrix[y0:y1, x0:x1])
    return out, (x0, y0, x1, y1)
