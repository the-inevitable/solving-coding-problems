"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""


def do_job(f, n):
    """
    Calls function f after n milliseconds.
    :param f: Function
    :param n: Numeric
    :return: None
    """
    import time
    time.sleep(n * 10**-3)
    f()


def job():
    print('Job is done.')


if __name__ == '__main__':
    do_job(job, 2000)
