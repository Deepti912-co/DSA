#NUMBER DIAMOND WITH XOR LOGIC

n=int(input("enter the value of n:"))
size=2*n-1
for i in range(size):
    for j in range(size):
        top=i
        left=j
        right=size-1-j
        bottom=size-1-i
        print(n-min(top,left,right,bottom), end=" ")
    print()
