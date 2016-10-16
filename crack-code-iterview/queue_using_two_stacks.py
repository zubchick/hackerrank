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

    def peek(self):
        if self.len():
            return self.data[-1]
        else:
            raise ValueError('Stack is empty')

    def len(self):
        return len(self.data)


class MyQueue(object):
    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def _rebalance(self):
        if not self.right.len():
            for _ in xrange(self.left.len()):
                value = self.left.pop()
                self.right.push(value)

    def peek(self):
        if self.right.len():
            return self.right.peek()

        self._rebalance()
        return self.right.peek()

    def pop(self):
        value = self.peek()
        self.right.pop()
        return value

    def put(self, value):
        self.left.push(value)


def main():
    queue = MyQueue()
    t = int(raw_input())
    for line in xrange(t):
        values = map(int, raw_input().split())

        if values[0] == 1:
            queue.put(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            print queue.peek()


if __name__ == '__main__':
    main()
