"""Model-facing contract for the pinned Astra drawing engine in PixelBench."""


def skill_tool_docs(vision=True, surface="full"):
    text = """Execute Python in the persistent ipykernel. Variables, canvases and imports survive calls.
Astra Pixel Art 0.6.0 drawing API (preloaded):
- canvas(ref) resolves an explicit name/index without selecting a default object.
- new_canvas(w,h,background=None,name=None) -> Canvas.
- canvases() lists canvases. One canvas is one layer; all share one palette.
- flatten([layers...],name=None,background=None) -> NEW Canvas, composited bottom-to-top.
- c.copy(name=None) copies pixels, shares palette; the copy is editable and directly submittable.
- input_canvas holds the supplied image (or the initial blank canvas for creation).
- For same-size edits, output = input_canvas.copy(name="output") preserves the exact input RGBA without compositing.
- c.select(x,y,w,h) -> Selection: snapshot a positive integer rectangle entirely inside c.
- s.flip(axis='h'|'v'), s.resize(width,height), s.rotate(angle,algorithm='nearest'|'rotsprite') -> NEW Selection; keep the returned recipe.
- Recipes always sample the original snapshot in flip/resize/rotate order. Resize sets absolute pre-rotation size; rotate sets absolute clockwise degrees; flip toggles. No cumulative resampling.
- s.size -> expanded (width,height); s.preview(name=None) -> detached Canvas; view(canvas=s.preview()) inspects it without submitting it.
- s.copy_to(x,y,canvas,mode='replace'), s.move_to(x,y,canvas,mode='replace') -> destination Canvas (explicit destination).
- Paste x/y is the absolute top-left of the expanded output; output clips. Replace includes selected transparent pixels, but rotated corners outside the selection leave destination untouched. mode='over' explicitly blends.
- Move clears the original rectangle and safely handles overlap; it rejects a changed source before writing. Reselect after moving. Copy keeps the original snapshot despite edits.
- Right-angle rotations are exact without resize; resize is nearest-neighbour. Optional RotSprite uses 8x Scale2x then rotate/sample, retaining original RGBA; arbitrary rotations/downscales may lose detail. Raster limit 16777216 pixels, including the 8x intermediate.
- Selection variables persist across code blocks but are not stored in saved canvas state. Preview/paste participate in drawing undo; recipe edits do not consume drawing checkpoints.
- c.color(spec,name=None) registers/looks up a colour, deduplicating RGBA; c.palette(), c.color_name(index).
- c.get(x,y) -> colour index. Colours accept registered names, indices, #rgb/#rrggbb/#rrggbbaa, RGB(A) tuples.
- c.set(x,y,colour); c.rect(x,y,w,h,colour,fill=True); c.line(x0,y0,x1,y1,colour).
- c.circle(cx,cy,r,colour,fill=True); c.ellipse(cx,cy,rx,ry,colour,fill=True).
- c.poly(points,colour,fill=True); c.path(svg_path_data,colour,fill=True).
- c.text(x,y,s,colour,spacing=None,font=None): built-in 5x7, 8px, 10px, 12px fonts; automatic ASCII 5x7 or Latin/CJK 12px.
- c.fill_at(x,y,colour); c.clear(x=0,y=0,w=None,h=None); c.blit(other_canvas,dx,dy).
- c.mirror(axis='h'); c.shift(dx,dy,fill=None); c.outline(colour).
- c.dither(x,y,w,h,[a,b],pattern='checker'|'bayer4').
- c.snapshot(name='default'); c.restore(name='default') save/restore that canvas's pixels.
- c.stats(), c.stats_text(); c.matrix_text(region=None,indices=False), region=(x0,y0,x1,y1) INCLUSIVE, with colour legend.
- save(name,canvas,scales=(1,4),indexed=False): native PNG, 4x PNG, reloadable state.
- load(path,name=None,add=True): PNG or skill state; export(name,layers,format='ase'|'ora'): layered document.
- undo_step() restores the last drawing API call, including canvases/palette.
- undo_round() restores the preceding code block's drawing state. Python variables/imports are NOT rolled back.
- finish(canvas) or finish([c1,c2,...]) freezes the supplied outputs in order, then ends the episode. Include all outputs requested by the task. Always pass Canvas objects inside run_code. No default target.
- redraw(canvas, rows) replaces an explicitly supplied canvas with a full matrix of colors.
- A copy has independent pixels but shares the palette. Later edits to the original pixels do not affect copies. A list holds references, not historical snapshots: copy() each frame before editing the next.
Drawing replaces pixels, including alpha; repeating a drawing call is idempotent.
None/'transparent' erases. Transparency means alpha == 0, not a special palette index.
Only flatten/blit and selection paste mode='over' blend source-over. Blends can add colours. You can register the colours you need.
Shapes fill by default, return the same Canvas for chaining, and never anti-alias.
Paths use SVG M/L/H/V/C/S/Q/T/A/Z, even-odd fill; fill=False strokes open paths unless closed with Z.
Coordinates: origin top-left, x right, y down; rect w/h are sizes. Out-of-canvas drawing clips and emits a non-blocking warning (once per canvas per execution); later operations still run.
Only the objects explicitly passed to finish are submitted. Use flatten([layers...]) explicitly to merge layers. A successful finish freezes pixels AND palette; later code cannot change the submission.
Failed code keeps mutations already executed (normal ipykernel semantics); use undo_round on the next call if needed.
Keep every frame as an editable Canvas; revise any frame before finish([f1,f2,...]). Failed finish validation leaves the episode open for repair.
"""
    if vision:
        text += """You are a multimodal model. view(canvas,scale=None,size=None,margin=None,edges='tl') emits a PNG to your vision module and returns its path.
Default view: transparent top/left margin, then long edge 512 with nearest-neighbour. scale and size are alternatives; margin=0 disables padding.
This is ONLY a preview transform: saved/submitted pixels stay at native size. Inspect the input first, then draw and inspect as needed.
"""
    else:
        text += "You cannot see images. Inspect c.matrix_text() (or a small region) and stats_text(); these return text, so print them. No image observation is fed to you.\n"
    if surface == 'redraw':
        text += "\nThis surface requires full-matrix redraw(canvas, rows) for pixel changes; partial drawing methods are disabled.\n"
    return text


def skill_system_prompt(vision=True, surface="full"):
    return (
        ("Use redraw(canvas, rows) for all pixel changes; partial drawing is disabled. " if surface == "redraw" else "") +
        "You are a pixel artist using the Astra Pixel Art object API in a persistent Python REPL. "
        "Create canvases with new_canvas(w,h), or copy input_canvas for edits. "
        "Canvas size is yours to choose and need not equal the input size: if the input is too small for "
        "the edit, register a larger canvas first, place the input image on it at a suitable position, "
        "then draw there. You may change the canvas size at any point while editing. "
        "Every drawing operation targets its Canvas object; there is no selected or default canvas. "
        "Organize layers, drafts and frames freely. Follow task dimensions and protected content. You can register the colours you need. "
        "When done, call finish(result) or finish([f1,f2,...]) inside run_code with the required number of objects. "
        + ("You are a multimodal model. Inspect images with view(canvas)." if vision else
           "You are text-only: print c.matrix_text() and c.stats_text(); no images are fed to you.")
    )


def skill_user_content(task):
    info = task.public_task()
    lines = [task.prompt, f"Task: {info['id']} ({info['task_type']}).",
             (f"Input image: {info['width']}x{info['height']} px." if task.task_type == "edit" else
              f"Required output: {info['width']}x{info['height']} px."),
             ('You can register the colours you need.' if task.task_type == 'edit' else
              f"Final visible-colour limit per image: {info['constraints']['max_colors']}; fully transparent pixels are free.")]
    if task.task_type in ('edit', 'restoration'):
        lines.append("The supplied image is input_canvas. Inspect it explicitly. output = input_canvas.copy(name='output') gives an exact, independently editable pixel copy.")
    else:
        lines.append("Create your drawing with new_canvas(w,h). input_canvas is also available as an initial blank canvas.")
    if task.task_type == 'edit':
        lines.append(
            "If you think your editing operations require a different canvas size, you may freely "
            "create canvases of different sizes with new_canvas(w,h). "
            "If the input canvas is too small to fit this motion or edit, "
            "create a larger canvas and place the input image at a suitable position before editing. "
            "If you discover during editing that the canvas is not large enough, you may adjust it "
            "at any time, including changing its size. To expand it, create a larger canvas and "
            "copy your existing work onto it with larger.blit(source, dx, dy)."
        )
        if max(1, task.num_frames or 1) > 1:
            lines.append(
                "The final frames should share the same canvas dimensions, which you may choose "
                "and revise during editing. The artwork and its parts may move as the action requires."
            )
    if task.task_type == 'restoration':
        lines.append("mask is a boolean NumPy array, indexed mask[y,x]. Only pixels inside mask may change. The undamaged reference is hidden; no comparison/score API is provided.")
    count = max(1, task.num_frames or 1)
    lines.append(f"Submit exactly {count} canvas(es) in task order: " +
                 ("finish(result)." if count == 1 else "finish([f1, f2, ...]). Keep frames editable until this final submission."))
    if task.frames_visible and task.frames:
        lines.append("reference_frames holds the supplied Canvas sequence; inspect individual objects with view(c) or print(c.matrix_text()).")
    if task.reference_visible and task.reference is not None and task.task_type != 'restoration':
        lines.append("reference holds the supplied reference Canvas; inspect it with view(reference) or print(reference.matrix_text()).")
    return [{'type': 'text', 'text': '\n'.join(lines)}]
