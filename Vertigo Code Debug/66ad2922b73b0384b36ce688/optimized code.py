from collections import Counter

if __name__ == "__main__":
    sample_list = [
        "desktop pc",
        "laptop",
        "desktop pc",
        "tablet",
        "laptop",
        "smartphone",
        "laptop",
        "tablet",
        "desktop pc",
        "smartphone",
    ]
    sample_string = "tablet"

    list_count = Counter(sample_list)
    string_count = Counter(sample_string)

    print("Count in list:", list_count)
    print("Count in string:", string_count)
