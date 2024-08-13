n=int(input())
sume=0
sumo=0
ar=list(map(int, input().split()))
for i in range(n):
    if ar[i]%2==0:
        sume=sume+ar[i]
    else:
        sumo=sumo+ar[i]
print("Sum of even numbers: ",sume)
print("Sum of odd numbers: ",sumo)
