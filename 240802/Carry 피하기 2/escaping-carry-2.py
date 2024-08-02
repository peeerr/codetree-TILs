def is_occur_carry(num1, num2, num3):
    num1, num2, num3 = adjust_digits(num1, num2, num3)
    
    for i, j, k in zip(num1, num2, num3):
        if i + j + k >= 10:
            return True
    return False


def adjust_digits(num1, num2, num3):
    num1, num2, num3 = list(str(num1)), list(str(num2)), list(str(num3))
    length = max(len(num1), len(num2), len(num3))

    for _ in range(length - len(num1)):
        num1.insert(0, 0)
    for _ in range(length - len(num2)):
        num2.insert(0, 0)
    for _ in range(length - len(num3)):
        num3.insert(0, 0)

    num1 = list(map(int, num1))
    num2 = list(map(int, num2))
    num3 = list(map(int, num3))

    return num1, num2, num3


n = int(input())
arr = [int(input()) for _ in range(n)]

res = -1

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not is_occur_carry(arr[i], arr[j], arr[k]):
                res = max(res, arr[i] + arr[j] + arr[k])

print(res)