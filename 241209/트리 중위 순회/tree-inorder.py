def inorder(i):
    global idx
    if i > n:
        return
    inorder(i * 2)
    tree[i] = inorder_result[idx]
    idx += 1
    inorder(i * 2 + 1)


k = int(input())
n = 2 ** k - 1
inorder_result = list(map(int, input().split()))

tree = [0 for _ in range(n + 1)]
idx = 0
inorder(1)

cnt, idx = 1, 1
while cnt <= 2 ** (k - 1):
    for _ in range(cnt):
        print(tree[idx], end=' ')
        idx += 1
    print()
    cnt *= 2
