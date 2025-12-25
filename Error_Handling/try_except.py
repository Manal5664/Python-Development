# Write a Python program to handle an error when the user enters
# invalid input while converting a string to an integer.

try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# Write a program to perform division of two numbers and handle the division by zero error.
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    res=a/b
    print(res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# Write a Python program to open a file and handle the case when the file does not exist.
try:
    file=open("data.txt","r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file does not Exist.")

# Write a program to access an element from a list and handle the IndexError.
try:
    list=[10,20,30,40,50]
    ind= int(input("Enter index: "))
    print(list[ind])
except IndexError:
    print("Error: Index out of range.")

# Write a Python program to access a value from a dictionary and handle the KeyError.
try:
    d={'name':'John','age':30 , 'city':'New York'}
    key=input("Enter key to access value: ")
    print(d[key])
except KeyError:
    print("Error: Key not found in dictionary.")



# Write a program that handles multiple exceptions such as ValueError and ZeroDivisionError.
try:
    a=int(input("Enter numerator: "))
    b=int(input("Enter denominator: "))
    res=a/b
    print(f"Result: {res}") 
except ValueError:
    print("Error: Invalid input! Please enter valid integers.")
except ZeroDivisionError:  
    print("Error: Division by zero is not allowed.")

# Write a Python program using try–except–else to validate user input.
try:
    num=int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")
else:
    print(f"You entered:", num)

# Write a program demonstrating the use of a finally block to execute code regardless of exceptions.
try:
    file=open("data.txt","r")
    content=file.read()
    print(content)  
except FileNotFoundError:
    print("Error: The file does not Exist.")
finally:
    print("Execution completed.")

# Write a Python program that catches a general exception using Exception and displays an error message.
try:
    a=int("abc")  # This will raise a ValueError
except Exception as e:
    print(f"An error occurred:", e)

# Write a program to handle an error that occurs during a mathematical operation (such as square root of a negative number).
import math
try:
    num=int(input("Enter a number: "))
    result=math.sqrt(num)
    print("Square root:", result)
except ValueError:
    print("Error: Cannot compute square root of a negative number.")