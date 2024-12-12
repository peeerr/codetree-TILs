import sys

MAX_INT = sys.maxsize


def find_nth(x):
    return x - (x // 3 + x // 5 - x // 15)


def parametric_search():
    left, right = 1, MAX_INT
    ans = MAX_INT

    while left <= right:
        mid = (left + right) // 2
        if find_nth(mid) >= n:
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1

    return ans


n = int(input())
print(parametric_search())
