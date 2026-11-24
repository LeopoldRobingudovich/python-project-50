from gendiff import generate_diff, parse_cli_args, parse_file


def main():
    args = parse_cli_args()
    dict1_from_json = parse_file(args.first_file)
    dict2_from_json = parse_file(args.second_file)
    formatted_diff = generate_diff(data1=dict1_from_json, data2=dict2_from_json)

    print(formatted_diff)


if __name__ == "__main__":
    main()
