# print all keys in the dictionary  std={"name":"ALi", "age":20, "class":"BS"}
std={"name":"ALi", "age":20, "class":"BS"}
for key in std:
    print(key)

# print all values in the dictionary
std={"name":"ALi", "age":20, "class":"BS"}
for value in std.values():
    print(value)

# using a while loop.
info={"a":1, "b":2, "c":3}
keys =list(info.keys())
l=0
while l < len(keys):
    print(keys[l])
    l+=1

# print all key-value pairs in the dictionary
record={"x":10, "y":20}
for key, value in record.items():
    print(key, value)

# count the number of keys in a dictionary using for loop
record={"x":10, "y":20, "z":30}
count = 0
for key in record:
    count += 1
print(count)
