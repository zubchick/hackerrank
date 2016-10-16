#!/usr/bin/env python
# coding: utf-8


class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self, default=None):
        if self.len() == 0:
            return default
        else:
            return self.data.pop()

    def len(self):
        return len(self.data)


def is_matched(expression):
    stack = Stack()
    pairs = {'}': '{', ')': '(', ']': '['}
    closes = set(pairs)
    opens = set(pairs.values())

    for br in expression:
        if br in opens:
            stack.push(br)
        elif br in closes:
            value = stack.pop()
            if value is None:
                return False
            if value != pairs[br]:
                return False
        else:
            return False
    if stack.len():
        return False

    return True


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        expression = raw_input().strip()
        if is_matched(expression) == True:
            print "YES"
        else:
            print "NO"


if __name__ == '__main__':
    main()
