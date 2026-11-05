import json


def parse_json(file_path: str) -> dict:
    with open(file_path, encoding='utf-8') as fp:
        return json.load(fp)
