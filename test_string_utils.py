import pytest

from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


class TestStringUtils:
    @pytest.mark.parametrize(
        "string, expected",
        [
            ("skypro", "Skypro"),
            ("Skypro", "Skypro"),
            ("123abc", "123abc"),
            ("", ""),
            (" привет", " привет"),
        ],
    )
    def test_capitalize(self, string_utils, string, expected):
        assert string_utils.capitalize(string) == expected

    @pytest.mark.parametrize(
        "string, expected",
        [
            (" skypro", "skypro"),
            ("   skypro", "skypro"),
            ("skypro", "skypro"),
            ("", ""),
            ("  ", ""),
            ("\tskypro", "\tskypro"),
        ],
    )
    def test_trim(self, string_utils, string, expected):
        assert string_utils.trim(string) == expected

    @pytest.mark.parametrize(
        "string, symbol, expected",
        [
            ("SkyPro", "S", True),
            ("SkyPro", "k", True),
            ("SkyPro", "U", False),
            ("", "a", False),
            ("skypro", "sky", True),
            ("skypro", "Sky", False),
        ],
    )
    def test_contains(self, string_utils, string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

    @pytest.mark.parametrize(
        "string, symbol, expected",
        [
            ("SkyPro", "k", "SyPro"),
            ("SkyPro", "Pro", "Sky"),
            ("SkyPro", "x", "SkyPro"),
            ("aaaa", "aa", ""),
            ("", "a", ""),
            ("banana", "na", "ba"),
        ],
    )
    def test_delete_symbol(self, string_utils, string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected
