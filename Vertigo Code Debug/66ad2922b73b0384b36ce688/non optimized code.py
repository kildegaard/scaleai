def custom_counter(iterable_list):
    count_dict = {}
    for item in iterable_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


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

    list_count = custom_counter(sample_list)
    string_count = custom_counter(sample_string)

    print("Count in list:", list_count)
    print("Count in string:", string_count)
