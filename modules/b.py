from f import total

def test_total()->None:
    assert total([1.0]) == 1.0
    assert total([]) == 0.0
