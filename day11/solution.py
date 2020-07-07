"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def solution1(s):
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in s:
        if char in brackets.keys():
            stack.append(char)
        else:
            if not stack:
                return False
            elif char != brackets.get(stack.pop()):
                return False
    # Will return True only if every appended element was popped out.
    return False if stack else True


if __name__ == '__main__':
    test_s1 = '([])[]({})'
    test_s2 = '([)]'
    test_s3 = '((()'

    print(solution1(test_s1))  # True
    print(solution1(test_s2))  # False
    print(solution1(test_s3))  # False
