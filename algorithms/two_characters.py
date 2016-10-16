#!/bin/python
# coding: utf-8
import sys
import re
from itertools import permutations


def is_valid(st):
    chars = set(st)
    if len(chars) != 2:
        return False

    x = st[0]
    y = st[1]
    if x == y:
        return False

    for i, ch in enumerate(st):
        if not i % 2:
            if ch != x:
                return False
        else:
            if ch != y:
                return False
    else:
        return True


def find_max(data):
    return len(max(data, key=len)) if data else 0


def _find(st):
    valid = {st} if is_valid(st) else set()

    size = find_max(valid)

    chars = set(st)
    for ch in chars:
        new_st = st.replace(ch, '')
        if len(new_st) > size:
            valid.update(find(new_st))

    return valid


def find(data):
    return find_max(_find(data))


def find2(data):
    candidats = []
    chars = set(data)
    variants = permutations(chars, 2)

    for var in variants:
        check = lambda x: bool(re.match(r'^({0}{1})+{0}?$'.format(*var), x))

        new = []
        ignore = chars - set(var)
        for ch in data:
            if ch not in ignore:
                new.append(ch)

        new = ''.join(new)
        if check(new):
            candidats.append(new)

    return find_max(candidats)

s = 'beabeefeab'
s_len = int(raw_input().strip())
s = raw_input().strip()
print find2(s)
