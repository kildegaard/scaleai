# Import the necessary modules
from __future__ import print_function
import bisect

try:
    raw_input
except NameError:
    raw_input = input


# Function for interpolation search using a while loop
def interpolation_search(sorted_collection, item):
    # Initialize the left and right pointers
    left = 0
    right = len(sorted_collection) - 1

    # Loop until the left pointer is less than or equal to the right pointer
    while left <= right:
        # Calculate the estimated position of the item using interpolation
        point = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left]
        )

        # Check if the calculated point is within the bounds of the collection
        if point < 0 or point >= len(sorted_collection):
            # If not, return None indicating that the item is not found
            return None

        # Get the item at the calculated point
        current_item = sorted_collection[point]
        # Check if the current item is the target item
        if current_item == item:
            # If so, return the point where the item is found
            return point
        else:
            # If not, adjust the pointers based on the comparison
            if item < current_item:
                # If the target item is less than the current item, move the right pointer to the left
                right = point - 1
            else:
                # If the target item is greater than the current item, move the left pointer to the right
                left = point + 1
    # If the loop ends without finding the item, return None
    return None


# Function for interpolation search using recursion
def interpolation_search_by_recursion(sorted_collection, item, left, right):
    # Calculate the estimated position of the item using interpolation
    point = left + ((item - sorted_collection[left]) * (right - left)) // (
        sorted_collection[right] - sorted_collection[left]
    )

    # Check if the calculated point is within the bounds of the collection
    if point < 0 or point >= len(sorted_collection):
        # If not, return None indicating that the item is not found
        return None

    # Check if the item at the calculated point is the target item
    if sorted_collection[point] == item:
        # If so, return the point where the item is found
        return point
    elif sorted_collection[point] > item:
        # If the item at the calculated point is greater than the target item, search in the left subarray
        return interpolation_search_by_recursion(
            sorted_collection, item, left, point - 1
        )
    else:
        # If the item at the calculated point is less than the target item, search in the right subarray
        return interpolation_search_by_recursion(
            sorted_collection, item, point + 1, right
        )


# Function to check if the collection is sorted
def __assert_sorted(collection):
    if collection != sorted(collection):
        raise ValueError("Collection must be sorted")
    return True


# Main program
if __name__ == "__main__":
    import sys

    # Get the input collection from the user
    user_input = raw_input("Enter numbers separated by comma:\n").strip()
    collection = [int(item) for item in user_input.split(",")]

    try:
        # Check if the collection is sorted
        __assert_sorted(collection)
    except ValueError:
        sys.exit("Sequence must be sorted to apply interpolation search")

    # Get the target item to be found from the user
    target_input = raw_input("Enter a single number to be found in the list:\n")
    target = int(target_input)

    # Perform the interpolation search
    result = interpolation_search(collection, target)

    # Print the result
    if result is not None:
        print("{} found at positions: {}".format(target, result))
    else:
        print("Not found")
