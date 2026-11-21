"""Provider-neutral generation defaults for the public harness."""
def generation_llm_config(config: dict) -> dict:
    cfg = dict(config)
    if cfg.get("api_format") == "responses":
        cfg.setdefault("temperature", None)
        cfg.setdefault("stream", True)
    return cfg
