import sys

MAX_INT = sys.maxsize


def is_possible(x):
    sum_x, lane = 0, 1

    for time in times:
        if time > x:
            return False

        sum_x += time

        if sum_x > x:
            lane += 1
            sum_x = time

    return lane <= m


n, m = map(int, input().split())
times = list(map(int, input().split()))

ans = MAX_INT
left, right = 1, MAX_INT

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)
