def get_three_smallest_product(numbers):
    if len(numbers) < 3:
        return -1
        
    sorted_nums = sorted(numbers)
    return sorted_nums[0] * sorted_nums[1] * sorted_nums[2]

n = int(input())
numbers = list(map(int, input().split()))

current_numbers = []
for num in numbers:
    current_numbers.append(num)
    result = get_three_smallest_product(current_numbers)
    print(result)
