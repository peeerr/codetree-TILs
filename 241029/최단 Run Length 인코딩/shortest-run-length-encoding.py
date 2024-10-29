import sys

def encode():
    temp = [a[0], 1]
    idx = 0

    for i in range(1, n):
        if temp[idx] == a[i]:
            temp[idx + 1] += 1
        else:
            temp.extend((a[i], 1))
            idx += 2
            
    return len("".join(list(map(lambda x : str(x), temp))))


a = list(input())
n = len(a)

ans = sys.maxsize

for _ in range(n):
    a.insert(0, a.pop())
    ans = min(ans, encode())

print(ans)