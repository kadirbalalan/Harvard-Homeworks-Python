from twttr import shorten

def test_shorten():
    assert shorten("hey") == "hy"
    assert shorten("haaaaaap") == "hp"
    assert shorten("hAaAan") == "hn"
    assert shorten("ha1") == "h1"
    assert shorten("HaAaN.") == "HN."