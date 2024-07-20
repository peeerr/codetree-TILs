a, b, c = map(int, input().split())

print(((a - 11) * 24 * 60) + ((b - 11) * 60) + (c - 11) if a >= 11 and b >= 11 and c >= 1 else -1)