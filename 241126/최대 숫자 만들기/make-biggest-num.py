from functools import cmp_to_key


def compare(a, b):
    if str(a) + str(b) > str(b) + str(a):
        return -1
    elif str(a) + str(b) < str(b) + str(a):
        return 1
    else:
        return 0


n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(key=cmp_to_key(compare))

print("".join(map(str, nums)))
