from gendiff import parse_cli_args, parse_json, generate_diff


def main():
    args = parse_cli_args()
    dict1_from_json = parse_json(args.first_file)
    dict2_from_json = parse_json(args.second_file)
    formatted_diff = generate_diff(data1=dict1_from_json, data2=dict2_from_json)  # ruff: ignore[unused-variable]

    print(formatted_diff)


if __name__ == "__main__":
    main()
