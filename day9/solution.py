"""
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox',
and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',
and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def solution(set_of_words, s):
    result = []
    limit = min(len(el) for el in set_of_words)
    while len(s) >= limit:
        word, idx, set_of_words = recursive(set_of_words, s)
        if word:
            result.append(word)
            s = s.replace(s[:idx], '', 1)
    return result


def recursive(sow, s):
    for idx in range(len(s) + 1):
        if idx == len(s):
            if s in sow:
                sow.remove(s)
                return s, idx, sow
        if s[:idx] in sow:
            sow.remove(s[:idx])
            return s[:idx], idx, sow


if __name__ == '__main__':
    test_set1 = ['quick', 'brown', 'the', 'fox']
    test_s1 = 'thequickbrownfox'

    test_set2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    test_s2 = 'bedbathandbeyond'

    test_set3 = ['you', 'application', 'for', 'your', 'thank']
    test_s3 = 'thankyouforyourapplication'

    print(solution(test_set1, test_s1))  # ['the', 'quick', 'brown', 'fox']
    print(solution(test_set2, test_s2))  # ['bed', 'bath', 'and', 'beyond']
    print(solution(test_set3, test_s3))  # ['thank', 'you', 'for', 'your', 'application']
