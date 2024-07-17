arr = [input().split() for _ in range(5)]

print("name")
for x in sorted(arr, key=lambda x : x[0]):
    print(" ".join(x))
print("\nheight")
for x in sorted(arr, key=lambda x : -float(x[1])):
    print(" ".join(x))