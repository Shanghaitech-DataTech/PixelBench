"""Curated smoke task set: 4 task types x sizes 16..48."""
from __future__ import annotations

from typing import List

from pixelbench.tasks.generators import AssetLibrary
from pixelbench.tasks.masks import blob_mask, rect_mask
from pixelbench.tasks.specs import TaskSpec

_LIB = AssetLibrary(seed=7)


def smoke_tasks() -> List[TaskSpec]:
    return [
        # --------------------------------------------- agentic (text2image)
        TaskSpec(
            id="direct_0001",
            task_type="agentic_creation",
            prompt="Create a 16x16 pixel art of a small red heart with a darker outline and a light shine highlight. Use at most 4 colors on a transparent background.",
            width=16,
            height=16,
            max_colors=4,
            metadata={"asset": "heart", "title": "Red heart icon"},
        ),
        TaskSpec(
            id="direct_0002",
            task_type="agentic_creation",
            prompt="Create a 24x24 pixel art of a gold coin with an embossed star in the center and a bright highlight. Use at most 6 colors on a transparent background.",
            width=24,
            height=24,
            max_colors=6,
            metadata={"asset": "coin", "title": "Gold coin"},
        ),
        # ------------------------------------------------------- agentic
        TaskSpec(
            id="agentic_0001",
            task_type="agentic_creation",
            prompt="Draw a 32x32 pixel art mushroom: red cap with white spots, cream stem, dark outline, subtle shading. Use at most 8 colors on a transparent background.",
            width=32,
            height=32,
            max_colors=8,
            metadata={"asset": "mushroom", "title": "Mushroom"},
        ),
        TaskSpec(
            id="agentic_0002",
            task_type="agentic_creation",
            prompt="Draw a 48x48 pixel art scene of a green tree with a brown trunk, a couple of fruit dots and a dark outline. Use at most 10 colors on a transparent background.",
            width=48,
            height=48,
            max_colors=10,
            metadata={"asset": "tree", "title": "Tree"},
        ),
        # ---------------------------------------------------- replication
        TaskSpec(
            id="replicate_0001",
            task_type="replication",
            prompt="Recreate the reference pixel art as accurately as possible on the 32x32 canvas. You may inspect the reference image, but there is no diff or score tool.",
            width=32,
            height=32,
            max_colors=12,
            reference=_LIB.generate("potion", 32, 32, seed=1),
            reference_visible=True,
            metadata={"asset": "potion", "title": "Potion bottle replication"},
        ),
        TaskSpec(
            id="replicate_0002",
            task_type="replication",
            prompt="Recreate the reference pixel art as accurately as possible on the 48x48 canvas. You may inspect the reference image, but there is no diff or score tool.",
            width=48,
            height=48,
            max_colors=16,
            reference=_LIB.generate("knight", 48, 48, seed=2),
            reference_visible=True,
            metadata={"asset": "knight", "title": "Knight replication"},
        ),
        # ---------------------------------------------------- restoration
        TaskSpec(
            id="restore_0001",
            task_type="restoration",
            prompt="A region of this 32x32 treasure chest has been erased. Restore the missing region so the chest looks complete and coherent. Do NOT modify any pixel outside the erased mask.",
            width=32,
            height=32,
            max_colors=10,
            reference=_LIB.generate("chest", 32, 32, seed=3),
            mask=rect_mask(32, 32, (8, 14, 16, 10)),
            metadata={"asset": "chest", "title": "Treasure chest restoration"},
        ),
        TaskSpec(
            id="restore_0002",
            task_type="restoration",
            prompt="A blob region of this 48x48 flower has been erased. Restore the missing pixels so the flower looks complete. Do NOT modify any pixel outside the erased mask.",
            width=48,
            height=48,
            max_colors=10,
            reference=_LIB.generate("flower", 48, 48, seed=4),
            mask=blob_mask(48, 48, 36, 18, r=9, seed=11),
            metadata={"asset": "flower", "title": "Flower restoration"},
        ),
        # ---------------------------------------------------------- edit
        TaskSpec(
            id="edit_0001",
            task_type="edit",
            prompt="The heart on the canvas is red. Change its main fill color to blue, keeping the outline and the shine highlight exactly as they are. Only touch the heart's fill pixels.",
            width=32,
            height=32,
            max_colors=12,
            base=_LIB.generate("heart", 32, 32, seed=5),
            metadata={"asset": "heart", "title": "Heart recolor"},
        ),
        TaskSpec(
            id="edit_0002",
            task_type="edit",
            prompt="This 48x48 mushroom has a red cap with white spots. Change ONLY the cap color from red to purple; keep the stem, spots, outline and background untouched.",
            width=48,
            height=48,
            max_colors=12,
            base=_LIB.generate("mushroom", 48, 48, seed=6),
            metadata={"asset": "mushroom", "title": "Mushroom cap recolor"},
        ),
    ]
