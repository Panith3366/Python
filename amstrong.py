n=int(input())
num=len(str(n))
ams=0
temp=n
while temp>0:
    d=temp%10
    ams+=d**num
    temp//=10
if ams==n:
    print("Yes")
else:
    print("No")