def find(start):
    end = start

    for i in range(start, n - 1):
        if arr[i] == arr[i + 1]:
            end += 1
        else:
            return end

    return end


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

while True:
    is_cut = False

    for start in range(n):
        end = find(start)

        if end - start + 1 >= m:
            is_cut = True
            arr[start : end + 1] = [0] * (end - start + 1)

            arr = list(filter(lambda x : x > 0, arr))
            n = len(arr)

    if not is_cut:
        break

print(n)
for i in range(n):
    print(arr[i])