n = int(input("Enter the number of terms: "))
a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
for i in range(n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c