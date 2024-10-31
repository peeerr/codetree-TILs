n = int(input())
jenga = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

temp1 = []
temp2 = []

for i in range(s1 - 1):
    temp1.append(jenga[i])
for i in range(e1, n):
    temp1.append(jenga[i])

for i in range(s2 - 1):
    temp2.append(temp1[i])
for i in range(e2, len(temp1)):
    temp2.append(temp1[i])

print(len(temp2))
for x in temp2:
    print(x)