import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# ---- Тесты для метода capitalize ----
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])

def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# ---- Тесты для метода trim ----
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro   ", "skypro   "),
    ("   04 апреля 2023", "04 апреля 2023"),
    ("нет пробелов", "нет пробелов"),
    (" ", ""),
    ("", ""),
    (None, None),
])
def test_trim_positive_and_negative(input_str, expected):
    if input_str is None:
        with pytest.raises(AttributeError):
            string_utils.trim(input_str)
    else:
        assert string_utils.trim(input_str) == expected

# ---- Тесты для метода contains ----
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "s", False),
    ("SkyPro", "P", True),
    ("SkyPro", "x", False),
    ("", "a", False),
    ("abc", "", True),
])
def test_contains_positive_and_negative(string, symbol, expected):
    result = string_utils.contains(string, symbol)
    assert result == expected

# ---- Тесты для метода delete_symbol ----
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaaa", "a", ""),
    ("abc", "x", "abc"),
    ("", "a", ""),
])

def test_delete_symbol_positive_and_negative(string, symbol, expected):
    result = string_utils.delete_symbol(string, symbol)
    assert result == expected

# ---- Негативные сценарии ----

    # trim
    def test_trim_with_none():
        assert utils.trim(None) is None

    # contains
    def test_contains_with_none():
        assert utils.contains(None, "a") is False
        assert utils.contains("abc", None) is False

    # delete_symbol
    def test_delete_symbol_with_none():
        assert utils.delete_symbol(None, "a") is None
        # Если второй аргумент None, метод возвращает исходную строку
        assert utils.delete_symbol("abc", None) == "abc"