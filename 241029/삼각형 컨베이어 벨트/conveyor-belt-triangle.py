n, t = map(int, input().split())
left = list(map(int, input().split()))
right = list(map(int, input().split()))
bottom = list(map(int, input().split()))

for _ in range(t):
    left_tmp = left[n - 1]
    right_tmp = right[n - 1]

    for i in range(n - 1, 0, -1):
        left[i] = left[i - 1]
    left[0] = bottom[n - 1]

    for i in range(n - 1, 0, -1):
        right[i] = right[i - 1]
    right[0] = left_tmp

    for i in range(n - 1, 0, -1):
        bottom[i] = bottom[i - 1]
    bottom[0] = right_tmp

print(*left)
print(*right)
print(*bottom)