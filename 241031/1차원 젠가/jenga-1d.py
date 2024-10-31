def cut(s, e):
    global n
    temp = []

    for i in range(s - 1):
        temp.append(jenga[i])
    for i in range(e, n):
        temp.append(jenga[i])
    
    n = len(temp)
    for i in range(n):
        jenga[i] = temp[i]


n = int(input())
jenga = [int(input()) for _ in range(n)]

for _ in range(2):
    s, e = map(int, input().split())
    cut(s, e)

print(n)
for i in range(n):
    print(jenga[i])