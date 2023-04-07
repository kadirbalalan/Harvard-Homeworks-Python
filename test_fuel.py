from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/5") == 60
    with pytest.raises(ValueError):
        convert("6/5")
    with pytest.raises(ZeroDivisionError):
        convert("6/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(60) == "60%"
