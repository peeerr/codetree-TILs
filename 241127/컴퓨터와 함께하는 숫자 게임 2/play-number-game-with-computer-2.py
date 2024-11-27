def binary_search(target):
    cnt = 1
    left, right = 1, m

    while left <= right:
        mid = (left + right) // 2

        if mid == target:
            return cnt
        elif mid > target:
            cnt += 1
            right = mid - 1
        else:
            cnt += 1
            left = mid + 1


m = int(input())
a, b = map(int, input().split())

min_cnt = m
max_cnt = 0

for i in range(a, b + 1):
    cnt = binary_search(i)
    min_cnt = min(min_cnt, cnt)
    max_cnt = max(max_cnt, cnt)

print(min_cnt, max_cnt)
