"""The creation protocol: budgets, the rerun rule and its classification of attempts."""
from PIL import Image

from pixelbench import protocol as P


def test_budgets_and_limits():
    assert P.WRITE_BUDGET == {"text2image": 25, "edit": 15}
    assert P.REQUEST_LIMIT_S == 75 * 60 and P.TASK_LIMIT_S == 3 * 3600


def opaque():
    im = Image.new("RGBA", (4, 4), (0, 0, 0, 0))
    im.putpixel((1, 1), (255, 0, 0, 255))
    return im


def test_classify():
    clear = Image.new("RGBA", (4, 4), (0, 0, 0, 0))
    assert P.classify("submitted", None, [], [opaque()]) == P.COMPLETE
    assert P.classify("submitted", None, [], []) == P.MODEL_FAILURE                     # no artwork
    assert P.classify("submitted", None, [], [clear, clear]) == P.MODEL_FAILURE          # only transparent frames
    assert P.classify("long_request_cut", None, [], [opaque()]) == P.MODEL_FAILURE      # cut off, even if recovered
    assert P.classify("episode_time_cut", None, [], [opaque()]) == P.MODEL_FAILURE
    assert P.classify("llm_error", "LLMError: Error code: 503", [], []) == P.INFRASTRUCTURE
    assert P.classify("llm_error", "LLMError: Error code: 429 - rate limit", [], [opaque()]) == P.INFRASTRUCTURE
    assert P.classify("llm_error", "APIConnectionError: Connection error.", [], []) == P.INFRASTRUCTURE
    assert P.classify("llm_error", "LLMError: Error code: 401", [], []) == P.FATAL
    assert P.classify("llm_error", "LLMError: Error code: 400 - bad request", [], [opaque()]) == P.COMPLETE


def test_rerun_rule():
    assert P.decide([]) == "rerun"
    assert P.decide([P.COMPLETE]) == "accept"
    assert P.decide([P.MODEL_FAILURE]) == "rerun"                       # one rerun ...
    assert P.decide([P.MODEL_FAILURE, P.MODEL_FAILURE]) == "accept"     # ... and the rerun counts
    assert P.decide([P.MODEL_FAILURE, P.COMPLETE]) == "accept"
    assert P.decide([P.INFRASTRUCTURE, P.INFRASTRUCTURE]) == "rerun"    # infrastructure: until it completes
    assert P.decide([P.INFRASTRUCTURE, P.MODEL_FAILURE]) == "rerun"     # the first model result still gets its rerun
    assert P.decide([P.MODEL_FAILURE, P.INFRASTRUCTURE, P.MODEL_FAILURE]) == "accept"
    assert P.decide([P.FATAL]) == "stop"
    assert P.decide([P.INFRASTRUCTURE] * 3, max_infrastructure_reruns=2) == "stop"
