"""
This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""
# cons(3, 4).__closure__[0].cell_contents is 3
# cons(3, 4).__closure__[1].cell_contents is 4


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    def return_first_element(*pargs):
        return pargs[0]
    return f(return_first_element)


def cdr(f):
    def return_second_element(*pargs):
        return pargs[1]
    return f(return_second_element)


if __name__ == '__main__':
    print(car(cons(3, 4)))  # 3
    print(cdr(cons(3, 4)))  # 4

    print(car(cons(13, 14)))  # 13
    print(cdr(cons(13, 14)))  # 14
