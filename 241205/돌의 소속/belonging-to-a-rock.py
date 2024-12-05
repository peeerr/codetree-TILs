n, q = map(int, input().split())
stones = [0] + [int(input()) for _ in range(n)]

one_dp = [0 for _ in range(n + 1)]
two_dp = [0 for _ in range(n + 1)]
three_dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if stones[i] == 1:
        one_dp[i] = one_dp[i - 1] + 1
        two_dp[i] = two_dp[i - 1]
        three_dp[i] = three_dp[i - 1]
    elif stones[i] == 2:
        two_dp[i] = two_dp[i - 1] + 1
        one_dp[i] = one_dp[i - 1]
        three_dp[i] = three_dp[i - 1]
    else:
        three_dp[i] = three_dp[i - 1] + 1
        one_dp[i] = one_dp[i - 1]
        two_dp[i] = two_dp[i - 1]

for _ in range(q):
    a, b = map(int, input().split())

    print(one_dp[b] - one_dp[a - 1], two_dp[b] - two_dp[a - 1], three_dp[b] - three_dp[a - 1])
    
