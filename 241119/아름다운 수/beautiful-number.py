def judge_happy():
    i = 0
    while i < n:
        num = lst[i]
        for j in range(i, i + num):
            if j >= n or lst[j] != num:
                return 0
            i = j + 1
    return 1


def choose(n):
    global ans

    if n == 0:
        ans += judge_happy()
        return

    for i in range(1, 5):
        lst.append(i)
        choose(n - 1)
        lst.pop()


n = int(input())
lst = []
ans = 0
choose(n)

print(ans)
