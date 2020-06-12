"""
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""


# Answer often lies in the test input and output data.
# O(N) time and O(1) space
def solution(numbers):
    prod = 1
    for i in numbers:
        prod = prod * i

    return [prod * (n**-1) for n in numbers]


if __name__ == '__main__':
    test_data1 = [1, 2, 3, 4, 5]
    test_data2 = [3, 2, 1]

    print(solution(test_data1))
    print(solution(test_data2))
