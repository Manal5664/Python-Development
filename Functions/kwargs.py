# what is **kwargs in Python?
# **kwargs allows a function to accept any number of keyword arguments.
# Inside the function, kwargs is treated as a dictionary.

# write a function using **kwargs that prints user profile info(name,email,age,city)
def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
user_profile(name="Alice", email="alice@gmail.com", age=30, city="New York")

# what will be the poutput of the following code?
def display(**kwags):
    print(kwags)
display(a=1, b=2, c=3)
# Output: {'a': 1, 'b': 2, 'c': 3}


# can **kwargs accept positional arguments? Explain why or why not
# No, **kwargs cannot accept positional arguments directly. 
# It is specifically designed to capture keyword arguments as a dictionary.
# Positional arguments are passed based on their position,
# while keyword arguments are passed based on their names.


# what happens if you pass a dictionary to a function without using **when the function
# except **kwargs?
# The entire dictionary is treated as one positional argument, which causes
# an error because the function expects keyword arguments.
def func(**kwargs):
    print(kwargs)
data = {'x': 10, 'y': 20}
# func(data)  # This will raise a TypeError

# Write a function using **kwargs that counts how many keyword arguments were passed.
def count_kwargs(**kwargs):
    return len(kwargs)
print(count_kwargs(a=1, b=2, c=3, d=4))  # Output: 4

# Write a function using **kwargs that counts how many keyword arguments were passed.
# Dictionary unpacking uses ** to break a dictionary into key–value pairs,
# which are then passed as keyword arguments to a function.

def show(**kwargs):
    print(kwargs)
data = {'name': 'Bob', 'age': 25}
show(**data)  # Output: {'name': 'Bob', 'age': 25}


