"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def solution(s):
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = [None]
    for char in s:
        if char in brackets.values() and char != brackets.get(stack.pop()):
            return False
        elif char in brackets.keys():
            stack.append(char)
    # Will return True only if every appended element was popped out.
    return len(stack) == 1


if __name__ == '__main__':
    test_s1 = '([])[]({})'
    test_s2 = '([)]'
    test_s3 = '((()'

    print(solution(test_s1))  # True
    print(solution(test_s2))  # False
    print(solution(test_s3))  # False
