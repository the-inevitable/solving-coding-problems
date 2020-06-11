"""
Problem statement:

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""


# O(n) time and space complexity
def do_numbers_add_up(numbers, k):
    # I had to such check as numbers.index(k-num) != idx:
    # for cases when k - num is present in the list
    # but it actually is the num (current iteration list element)
    # e.g. k = 20, num = 10, k - num = 10, 10 == num is True
    for idx, num in enumerate(numbers):
        if k - num in numbers and numbers.index(k-num) != idx:
            return True

    return False


if __name__ == '__main__':
    test_numbers_1 = [10, 15, 3, 7]
    test_k_1 = 17

    test_numbers_2 = [10, 15, 3, 7]
    test_k_2 = 18

    test_numbers_3 = [10, 15, 3, 7]
    test_k_3 = 19

    test_numbers_4 = [10, 15, 3, 7]
    test_k_4 = 20

    print(do_numbers_add_up(test_numbers_1, test_k_1))  # True
    print(do_numbers_add_up(test_numbers_2, test_k_2))  # True
    print(do_numbers_add_up(test_numbers_3, test_k_3))  # False
    print(do_numbers_add_up(test_numbers_4, test_k_4))  # False
