
n = int(input("Enter numeric character: "))
length = 1
while length ** 2 <= n:
    print(length ** 2)
    length += 1
    print("\nLast numeric character,"
          " elevated:", length - 1)
