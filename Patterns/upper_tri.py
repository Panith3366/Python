n=int(input())
for i in range(n):
    for j in range(n):
        if(j==n-1 or i-j==0 or i==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()