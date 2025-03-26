"""This is my dictionary test coding exercise!"""

__author__ = "730579218"

import pytest
from exercises.ex03.dictionary import invert


def test_invert_duplicate_value_error():
    """Edge case: raises KeyError when two keys map to the same value."""
    my_dictionary = {"kris": "jordan", "michael": "jordan"}
    with pytest.raises(KeyError):
        invert(my_dictionary)


def test_invert_two_pairs():
    """Use case: inverts a dictionary with two unique key-value pairs."""
    assert invert({"a": "x", "b": "y"}) == {"x": "a", "y": "b"}


def test_invert_three_pairs():
    """Use case: inverts a dictionary with three unique key-value pairs."""
    assert invert({"flower": "rose", "animal": "dog", "city": "charlotte"}) == {
        "rose": "flower",
        "dog": "animal",
        "charlotte": "city",
    }


from exercises.ex03.dictionary import count


def test_count_multiple_items():
    """Use case: counts multiple repeated items."""
    input_list = ["apple", "banana", "apple", "orange", "apple", "orange"]
    assert count(input_list) == {"apple": 3, "banana": 1, "orange": 2}


def test_count_all_unique():
    """Use case: counts when no repeated items."""
    input_list = ["pink", "blue", "yellow"]
    assert count(input_list) == {"pink": 1, "blue": 1, "yellow": 1}


def test_count_empty_list():
    """Edge case: handles an empty input list."""
    input_list = []
    assert count(input_list) == {}


from exercises.ex03.dictionary import favorite_color


def test_favorite_color_clear_winner():
    """Use case: returns the color that appears most frequently."""
    color_dict = {"Tim": "blue", "Bob": "pink", "Sally": "blue"}
    assert favorite_color(color_dict) == "blue"


def test_favorite_color_tie_returns_first():
    """Use case: returns the first color when there is a tie."""
    color_dict = {"Tim": "blue", "Bob": "pink", "Sally": "blue", "Henry": "pink"}
    assert favorite_color(color_dict) == "blue"


def test_favorite_color_entry():
    """Edge case: only one person in the dictionary."""
    color_dict = {"Hailey": "pink"}
    assert favorite_color(color_dict) == "pink"


from exercises.ex03.dictionary import bin_len


def test_bin_len_mixed_lengths():
    """Use case: bins strings of different lengths into correct sets."""
    input_list = ["the", "quick", "fox"]
    expected = {3: {"the", "fox"}, 5: {"quick"}}
    assert bin_len(input_list) == expected


def test_bin_len_duplicates():
    """Use case: uses a set to avoid duplicates."""
    input_list = ["rose", "tulip", "rose", "sunflower"]
    expected = {3: {"rose", "tulip", "sunflower"}}
    assert bin_len(input_list) == expected


def test_bin_len_empty_list():
    """Edge case: handles an empty input list."""


input_list = []
expected = {}
assert bin_len(input_list) == expected
