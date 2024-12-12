def binary_search(target):
    cnt = 0
    left, right = 1, m

    while left <= right:
        mid = (left + right) // 2
        if mid == target:
            return cnt + 1
        elif mid > target:
            right = mid - 1
        else:
            left = mid + 1
        cnt += 1


m = int(input())
a, b = map(int, input().split())

min_cnt, max_cnt = m, 0

for i in range(a, b + 1):
    cnt = binary_search(i)
    min_cnt, max_cnt = min(min_cnt, cnt), max(max_cnt, cnt)

print(min_cnt, max_cnt)
