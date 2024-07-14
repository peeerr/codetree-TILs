def f(i):
    if i == -1:
        return 0
    return max(f(i - 1), arr[i])

n = int(input())
arr = list(map(int, input().split()))
print(f(n - 1))