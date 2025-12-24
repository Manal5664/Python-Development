# Assignme Nested List Question


# 1. Given a = [[1, 2], [3, 4], [5]], write a for loop to print every element.
#    Draw the iteration table.
a = [[1, 2], [3, 4], [5]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])


# 2. For nums = [[10, 20, 30], [40], [50, 60]],
#    how many total iterations will the loop run?
nums = [[10, 20, 30], [40], [50, 60]]
count = 0
for sub in nums:
    for item in sub:
        count += 1
print("Total iterations:", count)


# 3. Write a program using for loop to find the sum of all numbers in
#    x = [[2, 4], [6, 8, 10]]. Draw each step.
x = [[2, 4], [6, 8, 10]]
total_sum = 0
for row in x:
    for val in row:
        total_sum += val
print("Sum:", total_sum)


# 4. Given matrix = [[1, 0], [0, 1]], print each row and column index.
matrix = [[1, 0], [0, 1]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print("Row:", i, "Column:", j)


# 5. For data = [[5], [6,7], [8,9,10]], print only even numbers.
#    Show iteration table.
data = [[5], [6,7], [8,9,10]]
for row in data:
    for val in row:
        if val % 2 == 0:
            print(val)


# 6. Find maximum value in nums = [[3,7], [2,9,1], [8]]
#    using nested for-loops.
nums = [[3,7], [2,9,1], [8]]
max_val = nums[0][0]
for row in nums:
    for val in row:
        if val > max_val:
            max_val = val
print("Maximum:", max_val)


# 7. Count how many elements are greater than 5 in lst = [[1,6], [7,2], [10]].
lst = [[1,6], [7,2], [10]]
count = 0
for row in lst:
    for val in row:
        if val > 5:
            count += 1
print("Greater than 5:", count)


# 8. Convert every element to its square in
#    x = [[2, 3], [4], [5, 6]]. Show before/after.
x = [[2, 3], [4], [5, 6]]
print("Before:", x)
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] = x[i][j] ** 2
print("After:", x)


# 9. For names = [['Ali', 'Sara'], ['Ahmed'], ['Saif', 'Zara']],
#    print each name length.
names = [['Ali', 'Sara'], ['Ahmed'], ['Saif', 'Zara']]
for group in names:
    for name in group:
        print(name, "Length:", len(name))


# 10. Write a for-loop to print the index path of each number
#     in grid = [[1,2,3],[4,5,6]].
grid = [[1,2,3],[4,5,6]]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print("Index path:", (i, j), "Value:", grid[i][j])


# 11. Using while loops, print all elements of a = [[4,5], [6,7,8]].
a = [[4,5], [6,7,8]]
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j])
        j += 1
    i += 1


# 12. Count total elements in nums = [[1], [2,3], [4,5,6]]
#     using while loops.
nums = [[1], [2,3], [4,5,6]]
count = 0
i = 0
while i < len(nums):
    j = 0
    while j < len(nums[i]):
        count += 1
        j += 1
    i += 1
print("Total elements:", count)


# 13. Using while loop, reverse-print elements of
#     lst = [[10,20], [30], [40,50]].
lst = [[10,20], [30], [40,50]]
i = len(lst) - 1
while i >= 0:
    j = len(lst[i]) - 1
    while j >= 0:
        print(lst[i][j])
        j -= 1
    i -= 1


# 14. Write a while loop program to find sum of each row
#     in x = [[3,3], [2,2,2], [1]].
x = [[3,3], [2,2,2], [1]]
i = 0
while i < len(x):
    row_sum = 0
    j = 0
    while j < len(x[i]):
        row_sum += x[i][j]
        j += 1
    print("Row sum:", row_sum)
    i += 1


# 15. For data = [[9], [8,7], [6,5,4]],
#     print only odd numbers using while.
data = [[9], [8,7], [6,5,4]]
i = 0
while i < len(data):
    j = 0
    while j < len(data[i]):
        if data[i][j] % 2 != 0:
            print(data[i][j])
        j += 1
    i += 1


# 16. Using while loop, find minimum value in
#     lst = [[12,5], [3,9,1]].
lst = [[12,5], [3,9,1]]
min_val = lst[0][0]
i = 0
while i < len(lst):
    j = 0
    while j < len(lst[i]):
        if lst[i][j] < min_val:
            min_val = lst[i][j]
        j += 1
    i += 1
print("Minimum:", min_val)


# 17. Using while loops, count how many numbers are divisible by 3
#     in nums = [[3,6], [2,9], [12]].
nums = [[3,6], [2,9], [12]]
count = 0
i = 0
while i < len(nums):
    j = 0
    while j < len(nums[i]):
        if nums[i][j] % 3 == 0:
            count += 1
        j += 1
    i += 1
print("Divisible by 3:", count)


# 18. Print the element positions (outer_idx, inner_idx)
#     for matrix = [[5], [6,7], [8,9]].
matrix = [[5], [6,7], [8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print((i, j))


# 19. Using while loop, multiply all numbers inside nested list:
#     x = [[1,2], [3], [4,5]].
x = [[1,2], [3], [4,5]]
product = 1
i = 0
while i < len(x):
    j = 0
    while j < len(x[i]):
        product *= x[i][j]
        j += 1
    i += 1
print("Product:", product)


# 20. Using while loops, convert all values into their cube
#     in nested = [[2], [3,4], [5]].
nested = [[2], [3,4], [5]]
i = 0
while i < len(nested):
    j = 0
    while j < len(nested[i]):
        nested[i][j] = nested[i][j] ** 3
        j += 1
    i += 1
print("Cubed:", nested)


# 21. How many levels deep is this list?
#     a = [1, [2, [3, [4]]]].
# Answer: 4 levels deep


# 22. Write a for-loop to flatten one level of nested list:
#     x = [[1,2], [3], [4,5]] → [1,2,3,4,5].
x = [[1,2], [3], [4,5]]
flat = []
for row in x:
    for val in row:
        flat.append(val)
print("Flattened:", flat)


# 23. Given data = [[1,[2,3]], [4,5]],
#     print only elements that are not lists.
data = [[1,[2,3]], [4,5]]
for row in data:
    for item in row:
        if not isinstance(item, list):
            print(item)


# 24. For grid = [[2,4,6], [1,3], [5]],
#     print sum of each row and then sum of all rows.
grid = [[2,4,6], [1,3], [5]]
total = 0
for row in grid:
    row_sum = sum(row)
    print("Row sum:", row_sum)
    total += row_sum
print("Total sum:", total)


# 25. For items = [['a','b'], ['c'], ['d','e','f']],
#     print length of each inner list and total length.
items = [['a','b'], ['c'], ['d','e','f']]
total_length = 0
for row in items:
    print("Inner length:", len(row))
    total_length += len(row) 
print("Total length:", total_length)
