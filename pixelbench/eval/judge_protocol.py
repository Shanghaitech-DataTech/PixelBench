"""PixelBench judge protocol v2: one prompt builder and one image pipeline.

Four cumulative protocol versions (experiments) are
defined here and share every piece of text and every preprocessing step, so
the only thing that differs between them is what the experiment turns on:

    e0_base      minimal prompt, native artwork, no margin
    e1_margin    + a 1/16 transparent margin on the left and top
    e2_rubric    + a scoring rubric conditioned on the task family and subject
    e3_reference + a reference image for the same task

Two things are task-type facts rather than optimisations, so they are on in
every experiment: an editing task always shows the original artwork, and a
material task is always previewed as a 2x2 tiling (a single tile cannot show
whether the tile is seamless).

Scale is deliberately not anchored. An earlier draft carried ten verbal
score bands; they inflated scores without improving ranking agreement, and the
paper no longer claims the 0-100 scale is absolutely meaningful, so they are
gone. The judge is a ranking instrument.

Every judge image is produced by:
    frames -> near-square grid -> [2x2 tile for materials] -> [margin]
           -> NEAREST scale so the longest side is 512, aspect preserved

The scale is intentionally left non-integer. Together with the 1/16 margin it
keeps the pixel grid from lining up with the vision encoder's patch grid: a
non-integer NEAREST scale spreads the blocks over slightly different widths, so
no patch can fall entirely inside one flat colour. Forcing a uniform integer
magnification restores exactly the alignment these two devices exist to break,
and measurably costs agreement.

Sources that are not on a pixel grid (GPT-Image-2, whether used as a reference
or scored as a probe) are fitted with LANCZOS instead.
"""
from __future__ import annotations

import io
import math
from dataclasses import dataclass, field
from typing import Literal, Sequence

from PIL import Image

PROTOCOL = "pixelbench_judge_v2"
JUDGE_SIZE = 512
MARGIN_DIVISOR = 16

Family = Literal["text2image", "edit", "animation", "multiview"]
FAMILIES: tuple[Family, ...] = ("text2image", "edit", "animation", "multiview")

# Subject categories of the 75 text2image tasks, as recorded in
# tasks/text2image/_index.json.
CATEGORIES = ("人物类", "生物类", "场景类", "物品类", "UI类", "材质类", "特效类")
CATEGORY_EN = {
    "人物类": "characters", "生物类": "creatures", "场景类": "scenes",
    "物品类": "objects", "UI类": "icons and interface elements",
    "材质类": "materials", "特效类": "effects",
}
TILED_CATEGORY = "材质类"


@dataclass(frozen=True)
class Experiment:
    key: str
    margin: bool
    rubric: bool
    reference: bool
    label: str


EXPERIMENTS: tuple[Experiment, ...] = (
    Experiment("e0_base", False, False, False, "minimal prompt, no margin"),
    Experiment("e1_margin", True, False, False, "+ 1/16 transparent margin"),
    Experiment("e2_rubric", True, True, False, "+ family and subject rubric"),
    Experiment("e3_reference", True, True, True, "+ reference image"),
)
EXPERIMENT_BY_KEY = {e.key: e for e in EXPERIMENTS}


# ---------------------------------------------------------------------------
# Image pipeline
# ---------------------------------------------------------------------------

def grid_shape(n: int, frame_w: int, frame_h: int) -> tuple[int, int]:
    """Columns and rows that pack n frames into the most nearly square block.

    Ties break towards fewer empty cells, then towards more columns, so a
    two-frame sequence stays side by side and reads in the intended order.
    """
    best = None
    for cols in range(1, n + 1):
        rows = math.ceil(n / cols)
        ratio = (cols * frame_w) / (rows * frame_h)
        key = (round(max(ratio, 1 / ratio), 6), cols * rows - n, -cols)
        if best is None or key < best[0]:
            best = (key, cols, rows)
    return best[1], best[2]


def compose_frames(
    frames: Sequence[Image.Image], *, smooth: bool = False,
    shape: tuple[int, int] | None = None,
) -> tuple[Image.Image, tuple[int, int]]:
    """Lay frames out in a grid; returns the image and (cols, rows).

    ``shape`` forces the layout. The caller fixes one layout per task, from the
    original canvas, so that a task's candidate and its reference are always
    arranged the same way and the prompt's ordering sentence describes both.
    Frames of unequal size are fitted into a common cell and centred, so a
    reference whose frames come from a different source still lines up.
    """
    assert frames, "at least one frame is required"
    images = [f.convert("RGBA") for f in frames]
    if len(images) == 1:
        return images[0], (1, 1)
    cell_w = max(f.width for f in images)
    cell_h = max(f.height for f in images)
    cols, rows = shape or grid_shape(len(images), cell_w, cell_h)
    assert cols * rows >= len(images), (shape, len(images))
    sheet = Image.new("RGBA", (cols * cell_w, rows * cell_h), (0, 0, 0, 0))
    resample = Image.Resampling.LANCZOS if smooth else Image.Resampling.NEAREST
    for i, frame in enumerate(images):
        if frame.size != (cell_w, cell_h):
            scale = min(cell_w / frame.width, cell_h / frame.height)
            frame = frame.resize((max(1, round(frame.width * scale)),
                                  max(1, round(frame.height * scale))), resample)
        x = (i % cols) * cell_w + (cell_w - frame.width) // 2
        y = (i // cols) * cell_h + (cell_h - frame.height) // 2
        sheet.alpha_composite(frame, (x, y))
    return sheet, (cols, rows)


def tile_2x2(image: Image.Image) -> Image.Image:
    """Repeat a seamless material tile 2x2, without gaps or flips."""
    w, h = image.size
    out = Image.new("RGBA", (2 * w, 2 * h), (0, 0, 0, 0))
    for x, y in ((0, 0), (w, 0), (0, h), (w, h)):
        out.paste(image, (x, y))
    return out


def add_margin(image: Image.Image) -> Image.Image:
    """Offset the artwork by 1/16 of its size on the left and top.

    This is the presentation step of e1. Shifting the artwork by a fraction of
    a magnified block stops the pixel grid from lining up with the vision
    encoder's patch grid, which on small canvases otherwise lets a whole patch
    fall inside one flat colour.
    """
    w, h = image.size
    left, top = max(1, w // MARGIN_DIVISOR), max(1, h // MARGIN_DIVISOR)
    out = Image.new("RGBA", (w + left, h + top), (0, 0, 0, 0))
    out.paste(image, (left, top))
    return out


def fit_longest(image: Image.Image, size: int = JUDGE_SIZE, *, smooth: bool = False) -> Image.Image:
    """Scale so the longest side is ``size``, preserving the aspect ratio.

    The scale factor is deliberately NOT forced to an integer. A non-integer
    NEAREST scale makes neighbouring pixel blocks land on slightly different
    widths (a 64x64 canvas gives a mix of 7px and 8px blocks), and that
    irregularity is the point of this step: it stops a vision patch from
    falling entirely inside one flat colour, which is what the 1/16 margin is
    also there to prevent. An integer magnification would restore exactly the
    alignment both devices exist to break.

    """
    scale = size / max(image.width, image.height)
    w = max(1, round(image.width * scale))
    h = max(1, round(image.height * scale))
    resample = Image.Resampling.LANCZOS if smooth else Image.Resampling.NEAREST
    return image.resize((w, h), resample)


def compose_native(
    frames: Sequence[Image.Image],
    *,
    margin: bool,
    tile: bool = False,
    smooth: bool = False,
    shape: tuple[int, int] | None = None,
) -> tuple[Image.Image, tuple[int, int]]:
    """Everything up to but not including magnification, so callers can share a scale."""
    image, shape = compose_frames(frames, smooth=smooth, shape=shape)
    if tile:
        image = tile_2x2(image)
    if margin:
        image = add_margin(image)
    return image, shape


def encode(image: Image.Image) -> bytes:
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()


def judge_png(
    frames: Sequence[Image.Image],
    *,
    margin: bool,
    tile: bool = False,
    smooth: bool = False,
    size: int = JUDGE_SIZE,
    shape: tuple[int, int] | None = None,
) -> tuple[bytes, tuple[int, int]]:
    """Full pipeline for one image."""
    image, shape = compose_native(frames, margin=margin, tile=tile, smooth=smooth, shape=shape)
    return encode(fit_longest(image, size, smooth=smooth)), shape


def to_native(image: Image.Image) -> Image.Image:
    """Undo a lossless integer nearest-neighbour enlargement, if there is one."""
    a = image.convert("RGBA")
    w, h = a.size
    best = 1
    for k in range(1, min(w, h) + 1):
        if w % k or h % k:
            continue
        small = a.resize((w // k, h // k), Image.Resampling.NEAREST)
        if small.resize((w, h), Image.Resampling.NEAREST).tobytes() == a.tobytes():
            best = k
    return a.resize((w // best, h // best), Image.Resampling.NEAREST)


# ---------------------------------------------------------------------------
# Prompt text. Every string below is sent verbatim; nothing is generated.
# ---------------------------------------------------------------------------

REPLY = "Reply with only one number from 0 to 100."

# --- task block ------------------------------------------------------------

T2I_TASK = "Task brief: {prompt}\nCanvas: {size}; max colors: {max_colors}"
EDIT_TASK = "Editing instruction: {prompt}\nOriginal canvas: {size}"

# Stated in every experiment: the environment lets the agent choose its own
# output canvas, so a size change is part of the task contract, not a defect.
EDIT_CANVAS_NOTE = (
    "The result may use a different canvas size or different margins from the original; "
    "that by itself is not a defect."
)
FRAME_LAYOUT = (
    "The result is a {n}-frame sequence shown as a single image, with the frames in order "
    "{order}."
)
# The task asks frame 1 to reproduce the original, which is already image 1 of
# this request, so it is not shown a second time.
FRAME_FIRST_WITHHELD_ONE = (
    "This task asks for {total} frames, of which the first reproduces the original. Only the "
    "remaining generated frame is shown."
)
FRAME_FIRST_WITHHELD_MANY = (
    "This task asks for {total} frames, of which the first reproduces the original. Only the "
    "remaining {n} generated frames are shown, in order {order}."
)
FRAME_ORDER = {"row": "left to right", "column": "top to bottom",
               "grid": "left to right, then top to bottom"}
TILE_NOTE = (
    "The image repeats the same native tile in a 2x2 grid, without gaps or flips, so that "
    "tile boundaries are visible. Regular repetition is not a defect."
)

# --- minimal scoring instruction (e0, carried by every later experiment) ---

T2I_MINIMAL = (
    "Rate this single pixel art image from 0 to 100 for overall quality for the task. " + REPLY
)
EDIT_MINIMAL = (
    "The first image is the original artwork. The last image is the result the model produced "
    "for this instruction. Rate the result from 0 to 100 for overall quality on this editing "
    "task. " + REPLY
)

# Optional e2 instruction for unchanged edit submissions. The paper's frozen
# e2 uses no family, so every arm adds exactly one change to the one before.
E2_EDIT_UNCHANGED_NOTE = (
    "If the submitted result is the same as the original artwork and does not perform "
    "the requested edit, treat it as a failed or incomplete submission and assign a low "
    "score, regardless of the original artwork's visual quality. For animation or "
    "multi-view tasks, judge the requested new frames or views; retaining an original "
    "frame when explicitly required is not itself a failure."
)
E2_EDIT_UNCHANGED_FAMILIES = ()

# --- e2 rubric: text2image, by subject -------------------------------------

T2I_RUBRIC = {
    "人物类": "Consider natural pose, an expressive silhouette and coherent anatomy. Favor "
              "harmonious colors, balanced shapes and a cohesive composition. The figure should "
              "read as a specific character: facial features clear and well proportioned, the "
              "hairstyle plausible, and the whole legible rather than cluttered.",
    "生物类": "Consider an appealing subject, expressive features, and a plausible design of form "
              "and movement. Favor harmonious colors, balanced shapes and a cohesive composition.",
    "物品类": "Prioritize whether the object is clear and recognizable: as pixel art it should be "
              "identifiable at a glance. Consider a recognizable silhouette, clear parts and "
              "balanced placement; shading is optional. Credit intentional simplicity; extra "
              "colors, shading or detail help only when they clarify form.",
    "场景类": "Prioritize whether the scene as a whole is clear and recognizable: spatial depth, "
              "coherent perspective, lighting, separation of foreground from background, and the "
              "visual appeal and decorative detail of the image. Credit intentional simplicity; "
              "extra colors, shading or detail help only when they clarify form.",
    "UI类": "Prioritize instant recognition at native size, a clear and conventional metaphor, the "
             "visual appeal of the icon, and clean separation from the background. When the task "
             "asks for a set, consistency of style, alignment, visual weight and sizing across the "
             "set matters as much as any single element.",
    "材质类": "Judge material identity, continuity across the tile boundaries, and the absence of "
              "abrupt seams or value breaks. The material should look natural and should not draw "
              "undue attention to itself, while still being attractive and clear.",
    "特效类": "Prioritize the overall shape of the effect, a readable sense of motion, energy or "
              "impact, a clear focal point, and shapes that express the phenomenon rather than a "
              "static decoration. Color ramps and contrast should support the effect's intensity.",
}
T2I_RUBRIC_ZH = {
    "人物类": "考虑自然的姿势、富有表现力的轮廓和连贯的解剖结构。偏好和谐的色彩、平衡的形状和统一的构图。"
              "人物形象展现角色特征，面部特征清晰，五官协调，发型合理，清晰而不杂乱。",
    "生物类": "考虑有吸引力的主体、富有表现力的特征，以及合理的形态和动作设计。"
              "偏好和谐的色彩、平衡的形状和统一的构图。",
    "物品类": "优先考虑物品是否清晰、可辨认，作为像素画让人一目了然是什么物品。考虑可辨识的轮廓、清晰的部分"
              "和平衡的摆放；阴影可选。认可有意的简洁；额外的颜色、阴影或细节只有在有助于明确形体时才有加分。",
    "场景类": "优先考虑整体场景是否清晰可辨认，空间深度、连贯的透视、光照、前景与背景的分离，以及画面的美观性"
              "与细节装饰。认可有意的简洁；额外的颜色、阴影或细节只有在有助于明确形体时才有加分。",
    "UI类": "优先考虑在原生尺寸下的即时识别、清晰且常规的隐喻、图标的美观程度，以及与背景的干净分离。"
             "当任务要求一套元素时，整套元素在风格、对齐、视觉重量和尺寸上的一致性与单个元素同等重要。",
    "材质类": "评判材质身份、跨图块边界的连续性，以及不存在突兀接缝或明度断裂。"
              "材质需要自然，不过多吸引注意，但需要美观清晰。",
    "特效类": "优先考虑特效整体的形状，可读的运动感、能量或冲击感，清晰的焦点，以及表达现象而非静态装饰的形状。"
              "色彩渐变和对比度应支持效果的强度。",
}
T2I_SIZE_SMALL = ("At this size, every pixel should be placed deliberately, so that it supports a "
                  "clear and appealing form.")
T2I_SIZE_LARGE = "Details should enrich the image while preserving clear forms."
T2I_SIZE_SMALL_ZH = "在此尺寸下，每个像素都应被合理安排，以支撑清晰、有吸引力的形体。"
T2I_SIZE_LARGE_ZH = "细节应丰富图像，同时保持清晰的形体。"
T2I_SIZE_THRESHOLD = 32

# --- e2 rubric: editing families -------------------------------------------

EDIT_RUBRIC = (
    "Weigh three things together.\n"
    "(1) Instruction compliance: does the result actually make the change the instruction asks "
    "for, on the right subject and to the right extent?\n"
    "(2) Preservation: do the character, objects, scene, style and palette that the instruction "
    "does not ask to change stay consistent with the original?\n"
    "(3) Craft: is the result clean and visually appealing pixel art?"
)
ANIMATION_RUBRIC = (
    "This is an action sequence, so also weigh:\n"
    "(4) Inter-frame continuity: do consecutive frames read as one continuous motion, holding the "
    "subject's identity, scale and placement steady between frames?\n"
    "(5) Pose plausibility: is the pose in each frame physically plausible for the described "
    "action, is the subject's movement and posture sound, and does the sequence express that "
    "action clearly?"
)
MULTIVIEW_RUBRIC = (
    "This is a multi-view turnaround, so also weigh:\n"
    "(4) Cross-view identity: do all views show the same character or object as the original, "
    "holding proportions, palette, costume and distinctive features consistent across views, and "
    "is each view a plausible projection of that same subject?"
)
EDIT_RUBRIC_ZH = (
    "综合权衡三件事。\n"
    "(1) 指令遵从：结果是否真正做出了指令要求的变化，作用在正确的对象上，且程度正确？\n"
    "(2) 保持：指令未要求改变的角色、物体、场景、风格和调色板是否与原作保持一致？\n"
    "(3) 工艺：结果是否是干净且视觉上吸引人的像素艺术？"
)
ANIMATION_RUBRIC_ZH = (
    "这是一个动作序列，因此还要权衡：\n"
    "(4) 帧间连续性：连续帧是否读起来像一段连续运动，并在帧与帧之间保持主体的身份、比例和位置稳定？\n"
    "(5) 姿势合理性：每一帧中的姿势对于所描述的动作是否物理上合理，角色的动作与姿势是否合理，"
    "序列是否清晰表达了该动作？"
)
MULTIVIEW_RUBRIC_ZH = (
    "这是一个多视角转身图，因此还要权衡：\n"
    "(4) 跨视角身份：所有视角是否都展示了与原作相同的角色或物体，并在各视角间保持比例、调色板、服装和"
    "显著特征一致，且每个视角都是同一主体的合理投影？"
)

# --- e3 reference ----------------------------------------------------------

REFERENCE_T2I = (
    "The next image is a reference for this task, generated by GPT-Image-2, a diffusion image "
    "model. It is not true pixel art: it does not lie on the pixel grid, and it uses its own "
    "resolution and proportions. Treat it only as one indication of what a visually strong result "
    "for this task can look like. Do not score the candidate on how closely it resembles the "
    "reference: the candidate's overall style and design may legitimately differ from it. Do not "
    "treat the reference as ground truth, and do not deliberately reward a drawing style that "
    "resembles it."
)
REFERENCE_EDIT_GT = (
    "The next image is a reference result for this task. It is one valid way to satisfy the "
    "instruction, not a target to copy, and a result that differs from it can be equally good or "
    "better. Use it only to gauge what a reasonable outcome for this instruction looks like. Do "
    "not score the result on how closely it resembles the reference."
)
REFERENCE_EDIT_GPTIMAGE = (
    "The next image is a reference for this task, generated by GPT-Image-2, a diffusion image "
    "model. It is not true pixel art: it changes the proportions and resolution of the original, "
    "and it does not lie on the pixel grid. Treat it only as a rough hint of an attractive visual "
    "outcome, not as a target to copy; a result that differs from it can be equally good or "
    "better. Do not score the result on how closely it resembles the reference: the result's "
    "overall style and design may legitimately differ from it. Do not treat the reference as "
    "ground truth, and do not deliberately reward a drawing style that resembles it."
)
REFERENCE_T2I_ZH = (
    "下一张图像是本任务的参考，由 GPT-Image-2（一个扩散图像模型）生成。它不是真正的像素艺术：它不在像素"
    "网格上，并使用自己的分辨率和比例。仅将其视为一种参考，表明该任务视觉上出色的结果可能是什么样。"
    "不要根据候选与参考的相似程度来评分，模型绘图的整体风格与设计可以与参考不同。"
    "不要将参考视为真值，也不要刻意奖励与参考图类似的绘画风格。"
)
REFERENCE_EDIT_GT_ZH = (
    "下一张图像是本任务的参考结果。它是满足该指令的一种有效方式，不是要复制的目标，与其不同的结果也可以"
    "同样好或更好。仅用它来衡量该指令的合理结果看起来是什么样。不要根据结果与参考的相似程度来评分。"
)
REFERENCE_EDIT_GPTIMAGE_ZH = (
    "下一张图像是本任务的参考，由 GPT-Image-2（一个扩散图像模型）生成。它不是真正的像素艺术：它改变了"
    "原作的比例和分辨率，并且不在像素网格上。仅将其视为一个吸引人的视觉结果的粗略提示，不是要复制的目标，"
    "与其不同的结果也可以同样好或更好。不要根据候选与参考的相似程度来评分，模型绘图的整体风格与设计可以"
    "与参考不同。不要将参考视为真值，也不要刻意奖励与参考图类似的绘画风格。"
)

# --- image captions --------------------------------------------------------

CAPTION_ORIGINAL = "Image 1, the original artwork:"
CAPTION_REFERENCE = "Image {n}, reference image (calibration aid, not the work being scored)."
CAPTION_CANDIDATE_T2I = "Candidate image (the work being scored):"
CAPTION_CANDIDATE_EDIT = "Image {n}, the model's result (the work being scored):"


@dataclass
class Message:
    """One assembled judge request: interleaved text and image slots."""
    text: str
    slots: list[tuple[str, str]] = field(default_factory=list)  # (kind, caption)

    def parts(self) -> list[dict]:
        out: list[dict] = [{"type": "text", "text": self.text}]
        for kind, caption in self.slots:
            out.append({"type": "text", "text": caption})
            out.append({"type": "image", "role": kind})
        return out


def size_guidance(width: int, height: int) -> str:
    return T2I_SIZE_SMALL if max(width, height) <= T2I_SIZE_THRESHOLD else T2I_SIZE_LARGE


# The English strings above are what the judge receives. The _ZH strings are the
# review copy and are never sent; this keeps the two sets from drifting apart
# silently by at least guaranteeing they cover the same keys.
MIRRORED = (
    (T2I_RUBRIC, T2I_RUBRIC_ZH),
)
for _en, _zh in MIRRORED:
    assert set(_en) == set(_zh), (set(_en) ^ set(_zh))
assert set(T2I_RUBRIC) == set(CATEGORIES)


def frame_order_phrase(shape: tuple[int, int]) -> str:
    cols, rows = shape
    if rows == 1:
        return FRAME_ORDER["row"]
    if cols == 1:
        return FRAME_ORDER["column"]
    return FRAME_ORDER["grid"]


def build_message(
    *,
    family: Family,
    experiment: Experiment,
    prompt: str,
    size: str,
    max_colors,
    category: str | None = None,
    width: int | None = None,
    height: int | None = None,
    n_frames: int = 1,
    frame_shape: tuple[int, int] = (1, 1),
    reference_kind: str | None = None,
    total_frames: int | None = None,
) -> Message:
    """Assemble the exact text and image order for one judge call.

    ``reference_kind`` is ``"gt"``, ``"gptimage"`` or ``None``; it is only
    consulted when the experiment enables the reference.
    """
    blocks: list[str] = []
    if family == "text2image":
        blocks.append(T2I_TASK.format(prompt=prompt, size=size, max_colors=max_colors))
    else:
        blocks.append(EDIT_TASK.format(prompt=prompt, size=size))

    facts = []
    if family != "text2image":
        facts.append(EDIT_CANVAS_NOTE)
    withheld = total_frames is not None and total_frames > n_frames
    if withheld and n_frames == 1:
        facts.append(FRAME_FIRST_WITHHELD_ONE.format(total=total_frames))
    elif withheld:
        facts.append(FRAME_FIRST_WITHHELD_MANY.format(
            total=total_frames, n=n_frames, order=frame_order_phrase(frame_shape)))
    elif n_frames > 1:
        facts.append(FRAME_LAYOUT.format(n=n_frames, order=frame_order_phrase(frame_shape)))
    if family == "text2image" and category == TILED_CATEGORY:
        facts.append(TILE_NOTE)
    if facts:
        blocks.append(" ".join(facts))

    scoring = [T2I_MINIMAL if family == "text2image" else EDIT_MINIMAL]
    if experiment.rubric:
        if family == "text2image":
            assert category in T2I_RUBRIC, category
            rubric = T2I_RUBRIC[category]
            if category not in ("UI类", "材质类", "特效类"):
                rubric += " " + size_guidance(width, height)
            scoring.insert(0, rubric)
        else:
            rubric = EDIT_RUBRIC
            if family == "animation":
                rubric += "\n" + ANIMATION_RUBRIC
            elif family == "multiview":
                rubric += "\n" + MULTIVIEW_RUBRIC
            scoring.insert(0, rubric)
    blocks.append("\n\n".join(scoring))
    if family in E2_EDIT_UNCHANGED_FAMILIES and experiment.key == "e2_rubric":
        blocks.append(E2_EDIT_UNCHANGED_NOTE)

    message = Message(text="\n\n".join(blocks))
    if family != "text2image":
        message.slots.append(("original", CAPTION_ORIGINAL))
    if experiment.reference and reference_kind:
        body = REFERENCE_T2I if family == "text2image" else (
            REFERENCE_EDIT_GT if reference_kind == "gt" else REFERENCE_EDIT_GPTIMAGE)
        head = CAPTION_REFERENCE.format(n=len(message.slots) + 1)
        message.slots.append(("reference", f"{head} {body}"))
    if family == "text2image":
        message.slots.append(("candidate", CAPTION_CANDIDATE_T2I))
    else:
        message.slots.append(("candidate", CAPTION_CANDIDATE_EDIT.format(n=len(message.slots) + 1)))
    return message
