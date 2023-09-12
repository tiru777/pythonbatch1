# List
"""
list is mutalable data strcture which allows indexing and duplicate values
and it will allow both homegenous and hetrogenous values to the list
- if we want to define emtpy list we have to use sqaure brackets [] or list keyword

x = [] # list
print(type(x))

#Methods
- append
- extend
- remove
- pop
- sort
- insert
- index
- clear
- count
"""
'''
# append
x = [3,4]
# 20 i need to add to list

x.append(20)
print(x)# [3, 4, 20]
x.append(60)
print(x)
'''
"""
# extend
x = [20,30,40,50]
y = [1,2,3,4]
'''
x.append(y)# [20,30,40,50,1,2,3,4]
print(x)# [20, 30, 40, 50, [1, 2, 3, 4]]
'''
x.extend(y)
print(x) #[20, 30, 40, 50, 1, 2, 3, 4]

# remove: specfic element remove 

x = [1,2,3,4,5,6,7]

x.remove(5)
print(x)# [1, 2, 3, 4, 6, 7]

# pop: it will remove default from right side to left side
x = [1,2,3,4,5,6,7]
x.pop()
print(x)
x.pop()
print(x)

#clear
x.clear()
print(x)#[]
# delete list
del(x)#it will delete variable of list data
x = [1,2,67,56,89,553,22,1,2,3,4,6.5]

x.sort(reverse=True) # descending order
print(x)
x.sort()# ascending order
print(x)
# insert

x = [1,2,3,4,5]
x.insert(2,20)# (list.insert(index.object))
print(x)
# assignmenets by using index
# Using insert based on sp index we can insert and earlier index value moved to next index
# but assignments it will replace
x = [1,2,3,4,5]
x[2]=30
print(x)#[1,2,30,4,5]
# index
x = [1,2,3,4,5]
print(x.index(4))#3
# count: to count specified element
x = [1,1,1,1,1,2,2,2,3,3,3,4,4,4]
print(x.count(1))
"""
'''
functions
- len()
- sum
- max
- min

x = [1,1,1,1,1,2,2,2,3,3,3,4,4,4]
print("sum:",sum(x))
print("length:",len(x))
print("max:",max(x))
print("min:",min(x))
'''

# sum of n lelements
x = int(input("enter the value:"))
y = 0

for i in range(x):#0,1,2,3,4
    y = y+ i # 0+0=0,#0+1=1 #1+2=3

print(y)








































