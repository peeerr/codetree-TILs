def check(i, j, k, a, b, c):
    if (abs(i - a) <= 2 or n - 2 <= abs(i - a) <= n - 1) and (abs(j - b) <= 2 or n - 2 <= abs(j - b) <= n - 1) and (abs(k - c) <= 2 or n - 2 <= abs(k - c) <= n - 1):
        return True
    return False


n = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

res = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if check(i, j, k, a1, b1, c1) or check(i, j, k, a2, b2, c2):
                res += 1

print(res)