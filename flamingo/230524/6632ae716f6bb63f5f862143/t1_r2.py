import csv
import argparse


def main(arg_values, arg_count):
    # Parse the arguments
    parser = argparse.ArgumentParser(description="Rename CSV columns")
    parser.add_argument("csv_file", help="Full path to the CSV file")
    parser.add_argument(
        "-n",
        "--new-names",
        help="New column names, comma-separated and enclosed in double quotes",
    )
    parser.add_argument(
        "-C",
        "--capitalize",
        action="store_true",
        help="Capitalize the first letter of each column name",
    )
    parser.add_argument(
        "-c",
        "--uppercase",
        action="store_true",
        help="Convert all column names to uppercase",
    )
    parser.add_argument(
        "-s",
        "--lowercase",
        action="store_true",
        help="Convert all column names to lowercase",
    )

    args = parser.parse_args(arg_values)

    # Check if the new column names argument was provided
    if args.new_names:
        new_column_names = [name.strip() for name in args.new_names.split(",")]
    else:
        new_column_names = None

    # Read the CSV file
    with open(args.csv_file, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)

    # Rename the columns
    if new_column_names:
        header = new_column_names
    elif args.capitalize:
        header = [name.capitalize() for name in header]
    elif args.uppercase:
        header = [name.upper() for name in header]
    elif args.lowercase:
        header = [name.lower() for name in header]

    # Write the updated CSV file
    with open(args.csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:], len(sys.argv) - 1)
