n=int(input())
for i in range(n):
    for j in range(n):
        if(i==n-1 or i==0 or i+j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()