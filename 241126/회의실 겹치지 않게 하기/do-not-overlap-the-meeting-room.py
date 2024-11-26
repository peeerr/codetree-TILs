n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x : x[1])

ans, last = 0, 0

for start, end in meeting:
    if last <= start:
        last = end
    else:
        ans += 1

print(ans)
