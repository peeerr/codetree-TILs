n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    arr[i] = [i + 1, arr[i]]

sorted_arr = sorted(arr, key=lambda x : (x[1], x[0]))

for x in arr:
    print(sorted_arr.index(x) + 1, end=' ')