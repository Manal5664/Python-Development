# Write mode 
with open('example.txt', 'w') as file:
    file.write('This is a sample text.\n')
    file.write('Writing to a file in write mode.\n')

# Read mode
with open('example.txt', 'r') as file:
    content = file.read()
    print('File Content:')
    print(content)
# Append mode
with open('example.txt', 'a') as file:
    file.write('Appending a new line to the file.\n')
# close the file is handled automatically by 'with' statement
# Read the updated file content
with open('example.txt', 'r') as file:
    updated_content = file.read()
    print('Updated File Content:')
    print(updated_content)# Open a file in different modes: write, read, and append

# opening a file in write mode
f=open('example.txt', 'w')
f.write('This is a sample text.\n')
f.write('Writing to a file in write mode.\n')
f.close()

# opening a file in read mode
f=open('example.txt', 'r')  # open use for connect the file
content = f.read()
print('File Content:')
print(content)
f.close() # close the file

# writeline()
# f=open('example.txt', 'w')
# lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
# f.writelines(lines)
# f.close()



from contextlib import contextmanager
@contextmanager
def open_file(file_name, mode):
    f = open(file_name, mode)
    try:
        yield f
    finally:
        f.close() 

with open_file('context.txt', 'w') as file:
    p=file.write('Adding a line using context manager.\n')

with open_file('context.txt', 'r') as file:
    content = file.read()
    print('Context Manager File Content:')
    print(content)  
