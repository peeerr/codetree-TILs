def is_possible(k):
    cnt = 0
    for x in arr:
        cnt += x // k
    return cnt >= m


def binary_search():
    left, right = 1, 100000
    max_num = 0

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            max_num = max(max_num, mid)
            left = mid + 1
        else:
            right = mid -  1

    return max_num


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

print(binary_search())
