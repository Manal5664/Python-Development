# print number form 1 to 10
i=0
while i <11:
    print(i)
    i += 1
# print number from 10 to 1 using for loop
for j in range(10,0,-1):
    print(j)

# loop through a list and print only items greater than 50
numbers = [10, 25, 50, 75, 100, 125]
for num in numbers:
    if num > 50:
        print(num)

# find the smallest number in a list USING loop
l=[9,2,3,7,1]
for i in l:
    smallest = l[0]
    if i < smallest:
        smallest = i
print("Smallest number is:",smallest)

# count vowels in a "python loop" using loop
string = "python loop"
vowels = "aeiou"
for char in string:
    if char in vowels:
        print(char) 
# count of vowels
count = 0
for char in string:
    if char in vowels:
        count += 1

print("Count of vowels is:", count)

# using nested loop to print each item in matrix=[[1,2,3],[4,5,6],[7,8,9]]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for items in row:
        print(items)

# using nested while loop, print all pairs (x,y) from:
# a=[1,2] and b=[3,4,5]
a = [1,2]
b = [3,4,5] 
i = 0
while i < len(a):
    j = 0
    while j < len(b):
        print((a[i], b[j]))
        j += 1
    i += 1

# multiply every element of a list _a_ with every element of another list _b_ 
a = [1,2]
b = [3,4,5]
result = []
for i in a:
    for j in b:
        result.append(i * j)

print("Resulting list:", result)

# from matrix=[[1,2,3],[4,5,6],[7,8,9]] print the sum of each inner list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    for items in row:
        sum_row=sum(row)
    print("Sum of",row,"is:",sum_row)


# count total elements in a nested list:num=[[10],[20,30],[40,50,60]].
num = [[10],[20,30],[40,50,60]]
count=0
for row in num:
    for items in row:
        count += 1
print("Total elements in nested list is:",count)

# print all keys and inner values from :
data= {'a': [1,2,3], 'b': [4,5,6]}
for key in data:
    for value in data[key]:
        print(key,value)

# print each character of each key keys from
d={'cat':1, 'dog':2}
for key in d:
    for char in key:
        print(char)

# print name and age from student dictionary:
std={'Ali':{'age':20},'sara':{'age':25}}

for key in std:
    for inner_key in std[key]:
        print("name",key,inner_key,std[key][inner_key])

# using nested loops, find total items in dictionary-of-lists:
info = {"x":[1],"y":[2,3],"z":[4,5,6]}
count= 0
for key in info: # x,y,z
    for item in info[key]: # [1], [2,3], [4,5,6]
        count += 1 #
print(count)

# convert dictionary keys in to list and print each index +key using while loop.
info = {"x":[1],"y":[2,3],"z":[4,5,6]}
l=list(info.keys())
index=0
while index<len(l):
    print(index,l[index])
    index += 1

# loop through a list and remove all odd numbers(create a new list)
numbers = [10, 15, 20, 25, 30, 35, 40]
even_numbers = []
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
print(even_numbers)

# using a while loop reverse the list
numbers = [10, 15, 20, 25, 30, 35, 40]
list=[]
index=len(numbers)-1
while index >=0:   
    list.append(numbers[index])
    index -= 1
print(list)
