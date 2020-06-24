"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
"""


def solution(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a


if __name__ == '__main__':
    print(solution(4))  # 5
    print(solution(8))  # 34
    print(solution(14))  # 510
