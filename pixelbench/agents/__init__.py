from pixelbench.agents.base import Agent, AgentResult, Budget
from pixelbench.agents.chat import LLMClient, LLMError
from pixelbench.agents.direct_agent import DirectGenAgent
from pixelbench.agents.mock import MockDirectAgent, MockREPLAgent, default_demo_script
from pixelbench.agents.repl_agent import REPLAgent
from pixelbench.agents.generation import generation_llm_config

__all__ = [
    "Agent",
    "AgentResult",
    "Budget",
    "LLMClient",
    "LLMError",
    "REPLAgent",
    "DirectGenAgent",
    "MockREPLAgent",
    "MockDirectAgent",
    "default_demo_script",
]


def _require_vision(cfg: dict, kind: str, name: str) -> bool:
    """Every evaluated model must explicitly register whether it is
    multimodal: the tool description differs (image options are only
    shown to vision-capable models)."""
    if "vision" not in cfg:
        raise ValueError(
            f"agent {name!r} (type {kind!r}) must register its vision capability: "
            'add "vision": true (multimodal) or "vision": false (text-only)'
        )
    return bool(cfg["vision"])


def build_agent(cfg: dict) -> Agent:
    """Instantiate an agent from a config dict (see config.py)."""
    kind = cfg.get("type", "repl")
    name = cfg.get("name", kind)
    if kind in ("mock-repl", "mock-file", "mock"):
        return MockREPLAgent(name=name, script=cfg.get("script"))
    if kind == "mock-direct":
        return MockDirectAgent(name=name, fallback_kind=cfg.get("fallback_kind", "heart"))
    if kind == "direct":
        return DirectGenAgent(
            name=name,
            llm=LLMClient.from_config(generation_llm_config(cfg.get("llm", cfg))),
            vision=_require_vision(cfg, kind, name),
            max_steps=cfg.get("max_steps"),
        )
    if kind in ("sdk-repl", "sdk-file"):
        from pixelbench.agents.sdk_adapter import AgentsSdkReplAgent

        llm = cfg.get("llm", cfg)
        return AgentsSdkReplAgent(
            name=name,
            model=cfg.get("model", "gpt-4o"),
            api_key=llm.get("api_key"),
            base_url=llm.get("base_url"),
            temperature=float(llm.get("temperature", 0.7)),
        )
    if kind in ("repl", "file"):
        return REPLAgent(
            name=name,
            llm=LLMClient.from_config(generation_llm_config(cfg.get("llm", cfg))),
            vision=_require_vision(cfg, kind, name),
            max_steps=cfg.get("max_steps"),
            # "full" (default) or "redraw" (whole-matrix redraws only, common for text-only
            # models). Set by "surface" in the config; the system prompt switches with it.
            surface=cfg.get("surface", "full"),
            instruction_role=cfg.get("instruction_role"),
        )
    raise ValueError(f"unknown agent type {kind!r}")
