from functools import cmp_to_key


def compare(a, b):
    if len(str(a)) == len(str(b)):
        if a > b:
            return -1
        elif a < b:
            return 1
        else:
            return 0
    else:
        if int(str(a) + str(b)) > int(str(b) + str(a)):
            return -1
        elif int(str(a) + str(b)) < int(str(b) + str(a)):
            return 1
        else:
            return 0


n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(key=cmp_to_key(compare))

print("".join(map(str, nums)))
