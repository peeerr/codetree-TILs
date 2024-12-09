def find_right_idx(start, end, root):
    for i in range(start, end + 1):
        if preorder_result[i] > root:
            return i
    return start + 1


def postorder(start, end):
    if start > end:
        return

    root = preorder_result[start]
    right_start = find_right_idx(start, end, root)

    postorder(start + 1, right_start - 1)
    postorder(right_start, end)
    print(root)


n = int(input())
preorder_result = [int(input()) for _ in range(n)]

postorder(0, n - 1)
