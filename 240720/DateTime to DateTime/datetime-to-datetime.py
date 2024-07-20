a, b, c = map(int, input().split())

diff = ((a * 24 * 60) + (b * 60) + c) - ((11 * 24 * 60) + (11 * 60) + 11)

print(diff if diff >= 0 else -1)