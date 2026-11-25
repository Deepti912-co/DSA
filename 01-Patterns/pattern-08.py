# INVERTED SQUARE PYRAMID

n=int(input("enter the value of n:"))
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    for j in range(n-i):
        print("*", end=" ")
    for j in range(n-i-1):
        print("*", end=" ")
    print()
