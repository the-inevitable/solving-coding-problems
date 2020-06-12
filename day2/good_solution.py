"""
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""


# Answer often lies in the test input and output data.
# O(N) time and O(1) space
def solution(numbers):
    product_list = list_product(numbers)
    return [int(product_list * (num**-1)) for num in numbers]


def list_product(lst):
    res = 1
    for n in lst:
        res = res * n
    return res


if __name__ == '__main__':
    test_data1 = [1, 2, 3, 4, 5]
    test_data2 = [3, 2, 1]

    print(solution(test_data1))
    print(solution(test_data2))
