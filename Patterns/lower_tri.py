n=int(input())
for i in range(n):
    for j in range(n):
        if(i==n-1 or i-j==0 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()