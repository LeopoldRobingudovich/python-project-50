from gendiff import generate_diff, parse_cli_args


def main():
    args = parse_cli_args()
    formatted_diff = generate_diff(
        file_path1=args.first_file, file_path2=args.second_file
    )

    print(formatted_diff)


if __name__ == "__main__":
    main()
