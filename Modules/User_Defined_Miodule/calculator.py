# Creating a User-defined Module
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
def power(a, b):
    res = a ** b
    print(res)
def square_root(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Cannot compute square root of negative number"
def factorial(n):
    if n < 0:
        return "Cannot compute factorial of negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    
if __name__ == "__main__":
    power(2, 4)
