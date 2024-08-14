n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    c=0
    for j in range(n):
        if a[i]==a[j]:
            c=c+1
    if c==1:
        l.append(a[i])
print(" ".join(map(str,l)))