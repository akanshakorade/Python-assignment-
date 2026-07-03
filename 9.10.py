largest = lambda a, b, c: a if a >= b and a >= c else (b if b >= c else c)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Largest =", largest(x, y, z))