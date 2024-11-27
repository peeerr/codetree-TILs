def calc(num):
    return num - (num // 3 + num // 5 - num // 15)


def binary_search():
    left, right = 1, 10 ** 9

    while left <= right:
        mid = (left + right) // 2

        while mid % 3 == 0 or mid % 5 == 0:
            mid += 1
            if mid > right:
                break

        if mid > right:
            right = left - 1
            continue

        idx = calc(mid)

        if idx == n:
            return mid
        elif idx > n:
            right = mid - 1
        else:
            left = mid + 1


n = int(input())
print(binary_search())
