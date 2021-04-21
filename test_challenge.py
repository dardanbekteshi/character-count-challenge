import challenge


def test_end_2_end():
    test_input = "aaaabbbcca"
    expected = [
        ("a", 4),
        ("b", 3),
        ("c", 2),
        ("a", 1)
    ]
    actual = challenge.count_chars_in_order(test_input)
    print(actual)
    assert actual == expected

    test_input = "aaaabbbccaacccbbbdd"
    expected = [
        ("a", 4),
        ("b", 3),
        ("c", 2),
        ("a", 2),
        ("c", 3),
        ("b", 3),
        ("d", 2)
    ]
    actual = challenge.count_chars_in_order(test_input)
    print(actual)
    assert actual == expected


def test_single_char():
    test_input = "aaaa"
    expected = [
        ("a", 4)
    ]
    actual = challenge.count_chars_in_order(test_input)
    assert actual == expected


def test_increase():
    item = challenge.Character("a", 0)
    item.increase()
    assert item.count == 1
    item.increase()
    assert item.count == 2
