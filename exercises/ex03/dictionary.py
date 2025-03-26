"""This is my dictionary coding exercise!"""

__author__ = "730579218"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    keys = list(dictionary)
    idx = 0

    while idx < len(keys):
        key = keys[idx]
        value = dictionary[key]

        dup_idx = 0
        result_keys = list(result)
        while dup_idx < len(result_keys):
            if result_keys[dup_idx] == value:
                raise KeyError("Duplicate value found when inverting!")
            dup_idx += 1

        result[value] = key
        idx += 1
    return result


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    idx = 0

    while idx < len(values):
        item = values[idx]

        if item in result:
            result[item] += 1
        else:
            result[item] = 1

        idx += 1
    return result


def favorite_color(color_dict: dict[str, str]) -> str:
    color_list = []

    for key in color_dict:
        color_list.append(color_dict[key])

    color_counts = count(color_list)

    max_count = 0
    fav_color = ""

    for key in color_dict:
        color = color_dict[key]
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            fav_color = color

    return fav_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result: dict[int, set[str]] = {}

    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}

    return result
