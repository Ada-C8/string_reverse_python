from string_reverse import string_reverse


def test_string_reverse_with_odd_number_of_characters():
    test_string = "Hello"

    assert string_reverse(test_string) == "olleH"


def test_string_reverse_with_even_number_of_characters():
    test_string = "Software"

    assert string_reverse(test_string) == "erawtfoS"


def test_string_reverse_returns_unmodified_if_input_is_empty_string():
    test_string = ""

    assert string_reverse(test_string) == ""


def test_string_reverse_returns_unmodified_if_input_is_None():
    test_string = None

    assert string_reverse(test_string) is None


def test_string_reverse_returns_unmodified_if_input_length_is_one():
    test_string = "?"

    assert string_reverse(test_string) == "?"


def test_string_reverse_with_long_string():
    test_string = (
        "Oh, Supercalifragelisticexpialidocious! Even though the sound of it "
        "is something quite atrocious. If you say it loud enough, you'll "
        "always sound precocious. Supercalifragelisticexpialidocious!")

    expected = (
        "!suoicodilaipxecitsilegarfilacrepuS .suoicocerp dnuos syawla ll'uoy "
        ",hguone duol ti yas uoy fI .suoicorta etiuq gnihtemos si ti fo dnuos "
        "eht hguoht nevE !suoicodilaipxecitsilegarfilacrepuS ,hO")

    assert string_reverse(test_string) == expected
