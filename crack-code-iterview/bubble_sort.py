#!/usr/bin/env python
# coding: utf-8


def sort(a):
    n = len(a)
    total_swaps = 0
    for i in xrange(n):
        swaps = 0
        for j in xrange(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
        total_swaps += swaps

        if swaps == 0:
            break
    print "Array is sorted in %s swaps." % total_swaps
    print "First Element: %s" % a[0]
    print "Last Element: %s" % a[-1]
    return a


def main():
    _ = input()
    a = map(int, raw_input().strip().split(' '))
    sort(a)


if __name__ == '__main__':
    main()
