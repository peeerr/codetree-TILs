def print_lst():
    print(*lst)


def choose(n):
    if n == 0:
        print_lst()
        return

    for i in range(1, k + 1):
        lst.append(i)
        choose(n - 1)
        lst.pop()


k, n = map(int, input().split())
lst = []
choose(n)
