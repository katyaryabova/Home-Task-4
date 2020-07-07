n = int(input("Enter number:"))
degree = 2
increase = 1
while degree <= n:
    degree *= 2
    increase += 1
print("degree in:", increase - 1, "result:", degree // 2)