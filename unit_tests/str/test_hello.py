from hello import hello

def test_default():
    assert hello() == "Hello, Blaire!"

def test_args():
    assert hello("David") == "Hello, David!"

def test_multiple():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}!"