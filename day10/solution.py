"""
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array,
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space.
You can modify the input array in-place and you do not need to store the results.
You can simply print them out as you compute them.
"""


def solution(lst: list, k: int):
    assert 1 <= k <= len(lst)

    for idx, el in enumerate(lst):
        if len(lst[idx:idx+k]) == k:
            print(max(lst[idx:idx + k]), end=' ')


if __name__ == '__main__':
    test_lst1 = [10, 5, 2, 7, 8, 7]
    test_k1 = 3

    solution(test_lst1, test_k1)  # 10 7 8 8
