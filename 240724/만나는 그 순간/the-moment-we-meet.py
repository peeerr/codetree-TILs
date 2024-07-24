def move(arr, moves):
    idx = 0
    for move in moves:
        direction, time = move[0], int(move[1])
        
        if direction == 'R':
            tmp = arr[idx] + 1
            arr.append(tmp); idx += 1
            for _ in range(time - 1):
                tmp += 1
                arr.append(tmp); idx += 1
        else:
            tmp = arr[idx] - 1
            arr.append(tmp); idx += 1
            for _ in range(time - 1):
                tmp -= 1
                arr.append(tmp); idx += 1


n, m = map(int, input().split())

a_moves = [input().split() for _ in range(n)]
b_moves = [input().split() for _ in range(m)]

a, b = [0], [0]

move(a, a_moves)
move(b, b_moves)

res = -1
for i in range(1, min(len(a), len(b))):
    if a[i] == b[i]:
        res = i
        break

print(res)