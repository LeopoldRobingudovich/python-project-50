import pytest
from gendiff.generate_diff import generate_diff
from gendiff.parsers import parse_json


def get_dict():
    dict1 = parse_json("tests/test_data/file1.json")
    dict2 = parse_json("tests/test_data/file2.json")
    return dict1, dict2


def test_diff():
    file_path = "tests/test_data/expected.txt"
    with open(file_path) as f:
        diff_str = f.read().strip()
        dict1, dict2 = get_dict()

    assert generate_diff(dict1, dict2) == diff_str
