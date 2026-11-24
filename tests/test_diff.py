from pathlib import Path

import pytest

from gendiff.generate_diff import generate_diff

JSON1 = "tests/test_data/file1.json"
JSON2 = "tests/test_data/file2.json"
YML1 = "tests/test_data/file1.yml"
YML2 = "tests/test_data/file2.yml"


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


@pytest.mark.parametrize(
    "file1,file2", [(JSON1, JSON2), (YML1, YML2)], ids=['json', 'yml']
)
def test_diff(file1: str, file2: str):
    diff_str = read_file('expected.txt').rstrip('\n')
    assert generate_diff(file1, file2) == diff_str
