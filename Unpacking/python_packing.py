# What will be the output of the following code?
a,b = 5,10
print(a,b)

# complete the code to unpack list values into variables
values = [1, 2, 3]
x, y, z = values
print(x, y, z)

# what error will this cause?
# a,b = [1, 2, 3]
# ValueError: too many values to unpack (expected 2)
# Fix the error by adjusting the number of variables

# unpack the first two values and ignore the kast using underscore
nums = [4, 5, 6]
m, n, _ = nums
print(m, n)

# what is the output?
a,*b = [7, 8, 9, 10]
print(a)  # Output: 7
print(b)  # Output: [8, 9, 10]

# unpack only the last value:
*c, d = [11, 12, 13, 14]
print(c)  # Output: [11, 12, 13]    
print(d)  # Output: 14

# predict the output
p, q, r = 'cat'
print(q)  # Output: 'a'

# why does given this error?
a,b = 'hi'
# no error occurs here because there are exactly two characters to unpack into two variables.
print(a,b)

# use unpacking to swap variables
x, y = 1, 2
x, y = y, x
print(x, y)  # Output: 2 1

# what will be printed?
data = (100, 200, 300,400,500)
a,*b,c =data
print(b)

