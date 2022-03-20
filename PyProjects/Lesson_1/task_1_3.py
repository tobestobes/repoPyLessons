n = input("Enter a number: ")

while n < '0':
    n = input("Please enter number greater then 0: ")

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")