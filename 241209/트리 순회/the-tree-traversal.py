def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(left[node])
    preorder(right[node])


def inorder(node):
    if node == '.':
        return
    inorder(left[node])
    print(node, end='')
    inorder(right[node])


def postorder(node):
    if node == '.':
        return
    postorder(left[node])
    postorder(right[node])
    print(node, end='')


n = int(input())
left, right = {}, {}

for _ in range(n):
    parent, left_child, right_child = input().split()
    left[parent] = left_child
    right[parent] = right_child

preorder('A')
print()
inorder('A')
print()
postorder('A')
