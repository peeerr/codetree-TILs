def f(i, j, k):
    if i == j:
        return k
    if k % arr[i] == 0:
        return f(i + 1, j, k)
    else:
        return f(0, j, k + 1)

n = int(input())
arr = list(map(int, input().split()))

print(f(0, n, max(arr)))