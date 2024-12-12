import sys 

MAX_INT = sys.maxsize


def is_possible(k):
    lane, sum_val = 1, 0
    for x in arr:
        sum_val += x
        if sum_val > k:
            lane += 1
            sum_val = x
    return lane <= m


def parametric_search():
    left, right = 1, MAX_INT
    ans = MAX_INT

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            ans = min(ans, mid)
            right = mid - 1
        else:
            left = mid + 1

    return ans


n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(parametric_search())
