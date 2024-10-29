n, t = map(int, input().split())
top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

for _ in range(t):
    top_tmp = top[-1]
    bottom_tmp = bottom[-1]

    for i in range(n - 1, 0, -1):
        top[i] = top[i - 1]
    top[0] = bottom_tmp

    for i in range(n - 1, 0, -1):
        bottom[i] = bottom[i - 1]
    bottom[0] = top_tmp

print(*top)
print(*bottom)