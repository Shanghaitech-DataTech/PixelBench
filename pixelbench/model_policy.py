"""Current reporting cohort. Archived outputs and original ratings remain immutable."""
EXCLUDED_MODELS = frozenset({'kimi-k2.7-code'})


def included_model(model: str) -> bool:
    normalized = model.strip().lower().replace('_', '-').replace(' ', '-')
    return normalized not in EXCLUDED_MODELS


def filter_ranking(ranking):
    """Remove retired conditions before assigning contiguous rank positions."""
    return [m for m in ranking if included_model(m) and m != "gpt-image-2"
            and not m.startswith("gpt-image-2-snapper")]


def filter_manifest(rec):
    rec = dict(rec)
    rec['models'] = {m: v for m, v in rec.get('models', {}).items() if included_model(m)}
    rec['results'] = [r for r in rec.get('results', []) if included_model(r.get('model', ''))]
    if 'summary' in rec:
        rec['summary'] = {**rec['summary'], 'ok': sum(bool(r.get('ok')) for r in rec['results']),
                          'fail': sum(not r.get('ok') for r in rec['results'])}
    return rec
