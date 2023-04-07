from plates import is_valid

def test_is_valid():
    assert is_valid(("HHHHHHHHHH")) == False
    assert is_valid(("0HH")) == False
    assert is_valid(("H")) == False
    assert is_valid(("AAA2AA")) == False
    assert is_valid("G") == False
    assert is_valid("G G") == False
    assert is_valid("G.G") == False
    assert is_valid("H6") == False
    assert is_valid("0AB") == False
    assert is_valid("AA,AA") == False
    assert is_valid("AA!AA") == False
    assert is_valid("AAA056") == False