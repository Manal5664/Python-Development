# Factorial of a number using recursion
# factorial(7)=7*6*5*4*3*2*1=5040
# factorial(0)=1
# factorial(n)=n*factorial(n-1) 

def factorial(n):
    if n==0 or n==1:  #base case
        return 1
    else:
        return n*factorial(n-1) #recursive case
print(factorial(7))  

print(factorial(0))
print(factorial(5))


# sum of list element
def sum (lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0]+sum(lst[1:]) #1: means from index 1 to end of list
print(sum([1,2,3,4,5]))
print(sum([]))
print(sum([10,20,30]))

# Fibonacci series using recursion
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))  # 0,1,1,2,3,5,8,13

# 0+1=1
# 1+2=3
# 2+3=5
# 3+5=8
# 5+8=13  

# Reverse a string using recursion
def rev_str(s):
    if len(s)==0:
        return ""
    else:
        return s[-1]+rev_str(s[:-1]) #s[:-1] means from index 0 to second last index
    
print(rev_str("string"))
print(rev_str(""))


# Power of a number using recursion
# pow_num(x,n)=x^n
def pow_num(x,n):
    if n==1 or n==0:
        return x
    else:
        return x * pow_num(x,n-1)
        
print(pow_num(3,7))
