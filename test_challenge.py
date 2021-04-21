import challenge


def test_empty_input():
    test_input = ""
    expected = []
    actual = challenge.count_characters(test_input)
    assert actual == expected


def test_single_char():
    test_input = "a"
    expected = [
        ("a", 1)
    ]
    actual = challenge.count_characters(test_input)
    assert actual == expected


def test_multiple_chars_of_same_type():
    test_input = "aaa"
    expected = [
        ("a", 3)
    ]
    actual = challenge.count_characters(test_input)
    assert actual == expected


def test_multiple_characters():
    test_input = "aaaabbbcca"
    expected = [
        ("a", 4),
        ("b", 3),
        ("c", 2),
        ("a", 1)
    ]
    actual = challenge.count_characters(test_input)
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
    actual = challenge.count_characters(test_input)
    print(actual)
    assert actual == expected


def test_increase_count():
    character = challenge.Character("a", 0)
    character.increase_count()
    assert character.count == 1
    character.increase_count()
    assert character.count == 2
