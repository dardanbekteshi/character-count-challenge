import challenge


def test_print():
    challenge.print_stuff()
    assert True


def test_end_2_end():
    test_input = "aaaabbbcca"
    expected = [
        ("a", 4),
        ("b", 3),
        ("c", 2),
        ("a", 4)
    ]
    actual = challenge.count_chars_in_order(test_input)
    assert actual == expected
