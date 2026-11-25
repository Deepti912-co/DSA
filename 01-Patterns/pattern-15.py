#PRINT A TRIANGLE OF UPPERCASE LETTERS WHERE EACH ROW STARTS WITH 'A', BUT THE NUMBER OF LETTERS DECREASES WITH EACH ROW

n=int(input("enter the value of n:"))
for i in range(n):
    for j in range(n-i):
        print(chr(65+j), end=" ")
    print()
