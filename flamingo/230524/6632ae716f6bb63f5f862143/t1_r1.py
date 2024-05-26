import csv
import argparse
import os


def main(arg_values, arg_count):
    if not os.path.exists(arg_values.file):
        print("The file does not exist. Please provide the correct path.")
        return

    if arg_values.new_columns is None:
        if arg_values.flag is None:
            print("Please provide new column names or use one of the flags: -C, -c, -s")
            return
        else:
            with open(arg_values.file, "r", encoding="latin-1") as f:
                reader = csv.reader(f)
                old_columns = next(reader)

            if arg_values.flag == "C":
                new_columns = [col.title() for col in old_columns]
            elif arg_values.flag == "c":
                new_columns = [col.upper() for col in old_columns]
            elif arg_values.flag == "s":
                new_columns = [col.lower() for col in old_columns]

    else:
        new_columns = [col.strip() for col in arg_values.new_columns.split(",")]

    data = []
    with open(arg_values.file, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the old header
        for row in reader:
            data.append(row)

    with open(arg_values.file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_columns)
        writer.writerows(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename CSV columns")
    parser.add_argument("file", type=str, help="CSV file path")
    parser.add_argument(
        "new_columns",
        type=str,
        nargs="?",
        default=None,
        help="New column names (comma-separated and enclosed in double quotes)",
    )
    parser.add_argument(
        "-C", action="store_const", dest="flag", const="C", help="Change to title case"
    )
    parser.add_argument(
        "-c", action="store_const", dest="flag", const="c", help="Change to uppercase"
    )
    parser.add_argument(
        "-s", action="store_const", dest="flag", const="s", help="Change to lowercase"
    )

    args = parser.parse_args()
    main(args, len(vars(args)))
