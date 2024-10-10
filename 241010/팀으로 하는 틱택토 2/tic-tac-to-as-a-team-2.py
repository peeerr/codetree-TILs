n = 3
arr = [list(map(int, list(input()))) for _ in range(n)]

visited = []
ans = 0

for i in range(n):
    for j in range(n):
        if i == 0 and set([arr[i][j], arr[i + 1][j], arr[i + 2][j]]) not in visited and len(set([arr[i][j], arr[i + 1][j], arr[i + 2][j]])) == 2:
            visited.append(set([arr[i][j], arr[i + 1][j], arr[i + 2][j]]))
            ans += 1

        if j == 0 and set([arr[i][j], arr[i][j + 1], arr[i][j + 2]]) not in visited and len(set([arr[i][j], arr[i][j + 1], arr[i][j + 2]])) == 2:
            visited.append(set([arr[i][j], arr[i][j + 1], arr[i][j + 2]]))
            ans += 1

        if i == 0 and j == 0 and set([arr[i][j], arr[i + 1][j + 1], arr[i + 2][j + 2]]) not in visited and len(set([arr[i][j], arr[i + 1][j + 1], arr[i + 2][j + 2]])) == 2:
            visited.append(set([arr[i][j], arr[i + 1][j + 1], arr[i + 2][j + 2]]))
            ans += 1

        if i == 0 and j == 2 and set([arr[i][j], arr[i + 1][j - 1], arr[i + 2][j - 2]]) not in visited and len(set([arr[i][j], arr[i + 1][j - 1], arr[i + 2][j - 2]])) == 2:
            visited.append(set([arr[i][j], arr[i + 1][j - 1], arr[i + 2][j - 2]]))
            ans += 1

print(ans)