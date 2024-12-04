def is_overlap(s1, e1, s2, e2):
    return e1 == s2 or e2 == s1 or s1 <= s2 <= e1 or s1 <= e2 <= e1


n = int(input())
infos = [(0, 0, 0)] + sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x : x[0])

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    s1, e1, p1 = infos[i]
    for j in range(i):
        s2, e2, _ = infos[j]
        if not is_overlap(s1, e1, s2, e2):
            dp[i] = max(dp[i], dp[j] + p1)

print(max(dp))
