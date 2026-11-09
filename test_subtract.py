from calculator import subtract


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5
