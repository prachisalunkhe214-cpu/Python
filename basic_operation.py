# Basic Operations in Python

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Arithmetic Operations
print("\n--- Arithmetic Operations ---")
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power =", a ** b)

# Comparison Operations
print("\n--- Comparison Operations ---")
print("a > b :", a > b)
print("a < b :", a < b)
print("a == b :", a == b)
print("a != b :", a != b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Assignment Operations
print("\n--- Assignment Operations ---")
x = a
x += b
print("After x += b :", x)

x -= b
print("After x -= b :", x)

x *= b
print("After x *= b :", x)

# Logical Operations
print("\n--- Logical Operations ---")
print("a > 0 and b > 0 :", a > 0 and b > 0)
print("a > 0 or b > 0 :", a > 0 or b > 0)
print("not(a > b) :", not(a > b))