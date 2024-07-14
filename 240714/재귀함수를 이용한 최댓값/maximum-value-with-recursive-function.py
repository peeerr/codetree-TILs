def f(i):
    if i == -1:
        return 0
    num = f(i - 1)
    return arr[i] if arr[i] > num else num

n = int(input())
arr = list(map(int, input().split()))
print(f(n - 1))