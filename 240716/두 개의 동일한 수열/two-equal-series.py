n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print('Yes' if sorted(a) == sorted(b) else 'No')