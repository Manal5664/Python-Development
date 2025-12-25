# what is *args in python?why is it ysed in functions definition?
# *args allows a function to accept any number of positional arguments.
# Inside the function, args is treated as a tuple.

# write a function using *args that accepts any number of integers
# and return the maximum value.
def find_max(*args):
    return max(args)

print(find_max(3, 7, 2, 9, 5))

# what will be the output of the following code?

def show(*args):
    print(args)

show(1, 'a', 3.5)
# All passed values are collected into a tuple named args

# Can *args accept zero arguments? Explain with an example.
# Yes, *args can accept zero arguments. In this case, it becomes an empty tuple.
def demo(*args):
    print(args)

demo()

# What is the difference between passing a tuple to a function and using *args?
# When passing a tuple to a function, the entire tuple is treated as a single argument.
# When using *args, each element of the tuple is treated as a separate positional argument. 
def func_with_tuple(t):
    print(t)

def func_with_args(*args):
    print(args)

my_tuple = (1, 2, 3)
func_with_tuple(my_tuple)  # Output: (1, 2, 3)  since the entire tuple is a single argument
func_with_args(*my_tuple)   # Output: (1, 2, 3) since each element is a separate argument

# Write a function using *args that concatenates multiple strings into a single string
def concatenate(*args):
    res=""
    for s in args:
        res+=s
    return res
print(concatenate("Hello", " ", "World", " !"))

# Explain how argument unpacking works with *args when passing a list or tuple to a function.
# Argument unpacking uses * to break a list or tuple into individual elements when passing it to a function.
# * while calling a function → unpacks
# *args inside a function → packs into a tuple
def show(a, b, c):
    print(a, b, c)

values = [10, 20, 30]
show(*values)

# Write a function count_args that accepts any number of arguments 
# using *args and returns how many arguments were passed.
def count_args(*args):
    return len(args)

print(count_args(1, 2, 3, 4, 5))  


# write a function average(*args) that accept any num return their average 
# if no arg are passed, return 0
def average(*args):
    if len(args)==0:
        return 0
    else:
        res=sum(args)/len(args)
        return res
    

average(5,9,8,9,6)


# what will be the output of the following code?
def test(*args):
    print(len(args))
    print(args)

values = (5, 10, 15)
test(*values)

# fix the following code using their arguement unpacking
def multiply(a, b, c):
    return a * b * c

nums = [2, 3, 4]
result = multiply(*nums) #nums is unpacked here
print(result)

# Write a function log_messages(level, *messages) such that:
# level is a string like "INFO" or "ERROR"
# messages can be any number of strings
# The function prints each message prefixed with the level
# Example Output:
# INFO: Server started
# INFO: Connection established

def log_messages(level,*messages):
    for msg in messages:
        print(f"{level}: {msg}")
log_messages("INFO", "Server started", "Connection established")

log_messages("ERROR", "File not found", "Access denied")

