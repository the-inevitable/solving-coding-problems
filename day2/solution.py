"""
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""


# O(N^2) time and O(N) space
def solution(numbers):
    new_arr = []
    for idx, num in enumerate(numbers):
        except_idx = (n for i, n in enumerate(numbers) if i != idx)
        new_arr.append(list_product(except_idx))
    return new_arr


def list_product(nums):
    result = 1
    for num in nums:
        result = result * num
    return result


if __name__ == '__main__':
    test_data1 = [1, 2, 3, 4, 5]
    test_data2 = [3, 2, 1]

    print(solution(test_data1))  # [120, 60, 40, 30, 24]
    print(solution(test_data2))  # [2, 3, 6]
