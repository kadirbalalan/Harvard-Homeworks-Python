from bank import value

def test_value():
    assert value("Hey") == 20
    assert value("hello dear") == 0
    assert value("good morning") == 100