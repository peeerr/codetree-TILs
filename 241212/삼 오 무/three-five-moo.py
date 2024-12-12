import sys

MAX_INT = sys.maxsize


def find_nth(x):
    return x - (x // 3 + x // 5 - x // 15)


def parametric_search():
    left, right = 1, MAX_INT
    while left <= right:
        mid = (left + right) // 2
        nth = find_nth(mid)
        if nth == n:
            return mid
        elif nth > n:
            right = mid - 1
        else:
            left = mid + 1


n = int(input())

print(parametric_search())
