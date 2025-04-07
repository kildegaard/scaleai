# def concat_integers(n):
#     return int(n * ((10**n) - 1) / 9)


# number = 14
# result = concat_integers(number)
# print(result)  # Output: 12345


def concat_integers(n):
    result = 0
    for i in range(1, n + 1):
        result = result * 10 + i
    return result


number = -5
result = concat_integers(number)
print(result)  # Output: 12345


# def concat_integers(n):
#     result = 0
#     multiplier = 1

#     for i in range(1, n + 1):
#         result += i * multiplier
#         multiplier *= 10

#     return result


# number = int(input("Enter an integer: "))
# concatenated = concat_integers(number)
# print(concatenated)


# def count_digits(x):
#     count = 0
#     while x > 0:
#         x //= 10
#         count += 1
#     return count


# def concatenate_numbers(n):
#     result = 0
#     for i in range(1, n + 1):
#         num_digits = count_digits(i)
#         result = result * (10**num_digits) + i
#     return result


# # Example usage:
# n = 15
# print(concatenate_numbers(n))
