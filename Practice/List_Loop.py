# write a loop to print each item of the list 
num=[2,4,6,8]
for i in num:
    print(i)


# using a while loop , print all items in colors list
colors = ['red', 'blue', 'green']
color=0
while color < len(colors):
    print(colors[color])
    color+=1

# print each number in a =[5,10,15,20] and also print "Done" after the loop ends
a=[5,10,15,20]
for i in a:
    print(i)
print("Done")

# print all even numbers from the list nums=[1,2,3,4,5,5,6] using for loop
nums=[1,2,3,4,5,6]
for i in nums:
    if i %2==0:
        print(i)


# count how many items are in data=[10,20,30,40,50] using while loop only
data=[10,20,30,40,50]
items=0
while items < len(data):
    items+=1
    print(items)

