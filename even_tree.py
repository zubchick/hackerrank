#!/usr/bin/env python
# coding: utf-8

from itertools import groupby


def build_matrix(n_vert, edges):
    matrix = [[0] * n_vert for _ in n_vert]
    for i, j in edges:
        matrix[i][j] = 1
        matrix[j][i] = 1

    return matrix


class Node(object):
    def __init__(self, data, children, count=0):
        self.data = data
        self.children = children
        self.children_count = count

    def _format(self):
        return (self.data, self.children_count,
                [i._format() for i in self.children])

    def __repr__(self):
        from pprint import pformat
        return 'Node' + pformat(self._format())


def build_tree(edges):
    edges = [sorted(i) for i in edges]
    edges.sort()
    res = {}

    for v, children in groupby(edges, lambda x: x[0]):
        res[v] = [i[1] for i in children]

    def _build(v):
        if v not in res:
            return 0, []

        total_count = 0
        children = []
        children_ids = res[v]
        for ch in children_ids:
            cnt, chld = _build(ch)
            total_count += cnt + 1
            node = Node(ch, chld, cnt)
            children.append(node)

        return total_count, children

    v = edges[0][0]
    count, children = _build(v)
    node = Node(v, children, count)

    return node


def find_split(node):
    res = []

    if (node.children_count + 1) % 2 == 0:
        res.append(node)

    for ch in node.children:
        res.extend(find_split(ch))

    return res


def main():
    n_vert, n_edge = map(int, raw_input().split())
    edges = []

    for _ in range(n_edge):
        edges.append([int(i) - 1 for i in raw_input().split()])

    node = build_tree(edges)
    split = find_split(node)
    print len(split) - 1


if __name__ == '__main__':
    main()
