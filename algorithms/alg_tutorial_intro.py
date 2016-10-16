to_find = raw_input()
_ = raw_input()
array = raw_input().split()

for i, chr in enumerate(array):
    if chr == to_find:
        print i
        break
