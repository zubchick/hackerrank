#!/usr/bin/env python
# coding: utf-8


def _fib(t1, t2):
    return t1 + t2 ** 2


def fib(t1, t2, n):
    for i in xrange(n - 2):
        t3 = _fib(t1, t2)
        t1, t2 = t2, t3

    return t3


def main():
    t1, t2, n = map(int, raw_input().split())
    print fib(t1, t2, n)


if __name__ == '__main__':
    main()
