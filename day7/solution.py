"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def solution(s, k):
    subs = []
    for idx1, char1 in enumerate(s):
        for idx2, char2 in enumerate(s[k:], k):
            if len(s[idx1:idx2]) and len(set(s[idx1:idx2])) <= k:
                subs.append(s[idx1:idx2])
    return max(subs, key=len), len(max(subs, key=len))


if __name__ == '__main__':
    test_s1 = 'abcba'
    test_k1 = 2

    test_s2 = 'abcdddddddddddddddddddddddddddddddddaaaaaazzzzzzzzzzzzzzzzzzzzba'
    test_k2 = 2

    print(solution(test_s1, test_k1))  # ('bcb', 3)
    print(solution(test_s2, test_k2))  # ('dddddddddddddddddddddddddddddddddaaaaaa', 39)
