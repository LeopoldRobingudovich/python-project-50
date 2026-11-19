from pathlib import Path

from gendiff.generate_diff import generate_diff
from gendiff.parsers import parse_json


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def get_dict():
    dict1 = parse_json("tests/test_data/file1.json")
    dict2 = parse_json("tests/test_data/file2.json")
    return dict1, dict2


def test_diff():
    diff_str = read_file('expected.txt').rstrip('\n')
    dict1, dict2 = get_dict()

    assert generate_diff(dict1, dict2) == diff_str


test_diff()
