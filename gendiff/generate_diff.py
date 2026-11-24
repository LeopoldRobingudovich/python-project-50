from gendiff.parsers import parse_file


def generate_diff(file_path1: str, file_path2: str) -> str:
    data1: dict = parse_file(file_path1)
    data2: dict = parse_file(file_path2)
    added = [
        ("+", key, value)
        for key, value in data2.items()
        if key not in data1 or data1[key] != value
    ]
    removed = [
        ("-", key, value)
        for key, value in data1.items()
        if key not in data2 or data2[key] != value
    ]
    unchanged = [
        (" ", key, value)
        for key, value in data1.items()
        if key in data2 and data2[key] == value
    ]

    sorted_differences = sorted(
        [*removed, *added, *unchanged], key=lambda elem: elem[1]
    )
    formatted_diff = (
        "{\n"
        + "\n".join(
            f"{sign} {key}: {value}" for sign, key, value in sorted_differences
        )
        + "\n}"
    )
    result_diff = formatted_diff.replace("True", "true").replace(
        "False", "false"
    )
    return result_diff
