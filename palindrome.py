n = int(input("Enter a number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
if n==rev:
    print("number is palindrome")
else:
    print("not palindrome")