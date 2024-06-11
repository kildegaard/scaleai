from __future__ import print_function
import bisect

try:
    raw_input
except NameError:
    raw_input = input


def interpolation_search(sorted_collection, item):
    # Initialize the left and right pointers for the search range
    left = 0
    right = len(sorted_collection) - 1

    # Continue the search while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the estimated position of the target item using interpolation
        point = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left]
        )

        # Check if the calculated point is within the bounds of the collection
        if point < 0 or point >= len(sorted_collection):
            return None

        # Get the item at the calculated point
        current_item = sorted_collection[point]

        # Check if the current item matches the target item
        if current_item == item:
            # Return the index of the found item
            return point
        else:
            # Adjust the search range based on the comparison
            if item < current_item:
                # Move the right pointer to the left of the current point
                right = point - 1
            else:
                # Move the left pointer to the right of the current point
                left = point + 1
    # Return None if the item is not found
    return None


def interpolation_search_by_recursion(sorted_collection, item, left, right):
    # Calculate the estimated position of the target item using interpolation
    point = left + ((item - sorted_collection[left]) * (right - left)) // (
        sorted_collection[right] - sorted_collection[left]
    )

    # Check if the calculated point is within the bounds of the collection
    if point < 0 or point >= len(sorted_collection):
        return None

    # Check if the item at the calculated point matches the target item
    if sorted_collection[point] == item:
        # Return the index of the found item
        return point
    elif sorted_collection[point] > item:
        # Recursively search in the left half
        return interpolation_search_by_recursion(
            sorted_collection, item, left, point - 1
        )
    else:
        # Recursively search in the right half
        return interpolation_search_by_recursion(
            sorted_collection, item, point + 1, right
        )


def __assert_sorted(collection):
    # Check if the collection is sorted
    if collection != sorted(collection):
        raise ValueError("Collection must be sorted")
    return True


if __name__ == "__main__":
    import sys

    # Get user input for the collection
    user_input = raw_input("Enter numbers separated by comma:\n").strip()
    collection = [int(item) for item in user_input.split(",")]

    try:
        # Verify that the collection is sorted
        __assert_sorted(collection)
    except ValueError:
        sys.exit("Sequence must be sorted to apply interpolation search")

    # Get user input for the target item
    target_input = raw_input("Enter a single number to be found in the list:\n")
    target = int(target_input)

    # Perform the interpolation search
    result = interpolation_search(collection, target)

    # Print the result
    if result is not None:
        print("{} found at positions: {}".format(target, result))
    else:
        print("Not found")
