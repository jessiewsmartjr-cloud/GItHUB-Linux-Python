import pytest

def test_parse_log_to_dict():
    log = "timestamp=2024-01-01 level=INFO msg='Started processing'"
    parsed = dict(item.split("=") for item in log.replace("'", "").split(" "))
    assert parsed["level"] == "INFO"
    assert parsed["msg"] == "Started processing"
