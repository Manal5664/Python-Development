# print each item of t=(3,6,9)
t=(3,6,9)
for i in t:
    print(i)

# print each item of t1=(10,20,30) along with its index
t1=(10,20,30)
index=0
for val in t1:
    print(val,index)
    index+=1

# write a while loop to print each item of t2=("a","b","c","d")
t2=("a","b","c","d")
items=0
while items < len(t2):
    print(t2[items])
    items+=1
# print last three items of tuple using for loop
tuple=(100,200,300,400,500)
for i in tuple[-3:]:
    print(i)
# summ all elemnts of marks.
marks=(45,67,89,23,78)
total=sum(marks)   
print("Total marks:",total)