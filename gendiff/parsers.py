import json

import yaml


def parse_file(file_path: str) -> dict:
    with open(file_path, encoding='utf-8') as fp:
        if file_path[-5:] == '.json':
            return json.load(fp)
        elif file_path[-5:] == '.yaml' or file_path[-4:] == '.yml':
            return yaml.safe_load(fp)

        raise ValueError(f"Unsupported format {file_path}")
