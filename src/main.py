from utils import addition, subtructor, multiply, divide

name = "Mahmudul Hasan Shiblee"

Date = "13th June, 2026"

print(f"My name is {name}")
print(f"Date: {Date}")

summing_res = addition(29, 1)
sub_res = subtructor(10, 5)

multi = multiply(4, 5)
div = divide(100, 10)

print(f"Sum: {summing_res}")
print(f"Sub: {sub_res}")
print(f"Multiply: {multi}")
print(f" Divide: {div}")


# Error Handling Test
print("\n--- Error Handling Test ---")
try:
    print(f"50 / 0 = {divide(50, 0)}")
except ValueError as e:
    print(f"Error: {e}")


# Subtraction error handling
try:
    print(f"10 - 'hello' = {subtract(10, 'hello')}")
except TypeError as e:
    print(f"Error: {e}")
