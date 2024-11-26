import pytest
from string_utils import StringUtils

processor = StringUtils()

@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("текст", "Текст"), #позитивная
        ("", "") #негативная
    ],
)
def test_capitilize_positive_and_negative(input_text, expected_output):
    assert processor.capitilize(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("   Текст", "Текст"), #позитивная
        ("    ", "") #негативная
    ],
)
def test_trim_positive_and_negative(input_text, expected_output):
    assert processor.trim(input_text) == expected_output


@pytest.mark.parametrize(
    'string, delimeter, result',
    [
        ("1:2:3", ":", ['1', '2', '3']), #позитивная
        ("№|?,11/#", "/", ['№|?,11', '#']), #позитивная
        ("   ", "", []), #негативная
        (None, "", []) #негативная
    ],
)
def test_to_list_positive_and_negative(string, delimeter, result):
        res = processor.to_list(string, delimeter)
        assert res == result


@pytest.mark.parametrize(
    'string, symbol, result',
    [
        ("Текст", "с", True), #позитивная
        ("Текст", "о", False), #негативная
        ("  ", "о", False), #негативная
        ("Текст", "5", False), #негативная
    ],
)
def test_contains_positive_and_negative(string, symbol, result):
    res = processor.contains(string, symbol)
    assert res == result


@pytest.mark.parametrize(
    'string, symbol, result',
    [
        ("Текст", "Т", "екст"), #позитивная
        ("Текст", "Тек", "ст"), #позитивная
        ("Текст", "#", "Текст") #негативная
    ],
)
def test_delete_symbol_positive_and_negative(string, symbol, result):
    res = processor.delete_symbol(string, symbol)
    assert res == result


@pytest.mark.parametrize(
    'string, symbol, result',
    [
        ("Текст", "Т", True), #позитивная
        ("Текст", "Р", False) #негативная
    ],
)
def test_starts_with_positive_and_negative(string, symbol, result):
    res = processor.starts_with(string, symbol)
    assert res == result


@pytest.mark.parametrize(
    'string, symbol, result',
    [
        ("Текст", "т", True), #позитивная
        ("Текст", "р", False) #негативная
    ],
)
def test_end_with_positive_and_negative(string, symbol, result):
    res = processor.end_with(string, symbol)
    assert res == result


@pytest.mark.parametrize(
    'string, result',
    [
        ("", True), #позитивная
        ("   ", True), #позитивная
        ("Текст", False) #негативная
    ],
)
def test_is_empty_positive_and_negative(string, result):
    res = processor.is_empty(string)
    assert res == result


@pytest.mark.parametrize(
    'lst, joiner, result',
    [
        ([1,2,3,4], "", "1, 2, 3, 4"), #позитивная
        (['Sky','Pro'], "", "Sky, Pro"), #позитивная
        (['Sky','Pro'], "-", "Sky-Pro") #позитивная
    ],
)
def test_list_to_string_positive_and_negative(lst, joiner, result):
    res = processor.list_to_string(lst, joiner)
    assert res == result