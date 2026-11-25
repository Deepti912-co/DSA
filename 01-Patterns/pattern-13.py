# PRNT A TRIANGLE OF CONSECUTIVE NUMBERS

n=int(input("enter the vlaue of n:"))
num=1
for i in range(n):
    for j in range(i+1):
        print(num, end=" ")
        num+=1
    print()
