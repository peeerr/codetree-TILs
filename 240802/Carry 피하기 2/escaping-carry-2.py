def is_occur_carry(num1, num2, num3):
    if (num1 % 10) + (num2 % 10) + (num3 % 10) >= 10:
        return True
    elif (num1 // 10 % 10) + (num2 // 10 % 10) + (num3 // 10 % 10) >= 10:
        return True
    elif (num1 // 100 % 10) + (num2 // 100 % 10) + (num3 // 100 % 10) >= 10:
        return True
    elif (num1 // 1000 % 100) + (num2 // 1000 % 100) + (num3 // 1000 % 100) >= 10:
        return True

    return False


n = int(input())
arr = [int(input()) for _ in range(n)]

res = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not is_occur_carry(arr[i], arr[j], arr[k]):
                res = max(res, arr[i] + arr[j] + arr[k])

print(res)