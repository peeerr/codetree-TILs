n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = [i + 1, arr[i]]

sorted_arr = sorted(arr, key=lambda x : (x[1], x[0]))

def idx(n, arr):
    for i, x in enumerate(arr):
        if x == n:
            return i

for x in arr:
    print(idx(x, sorted_arr) + 1, end=' ')