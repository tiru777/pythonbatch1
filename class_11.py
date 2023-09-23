# set
# either set() keyword or coma seprated culry braces {,}
# mutable type of data structure
# it wont allow duplicates
# it won't allow indexing
# it is homogenous and hetrogenous
'''
x = set()
print(type(x))# <class 'set'>

x = {1,2,3}
# add
x.add(20)
print(x)

# update
x = {1,2,3}
y = {30,40,60}
x.update(y)# {1, 2, 3, 40, 60, 30}
print(x)
# it won't duplicates
x = {1,1,1,1,2,2,3,3,4,4}
print(x)# {1, 2, 3, 4}

# union
x = {1,2,3,4,5,6}
y = {4,5,6,30,40,60}
z = x.union(y)# {1, 2, 3, 40, 60, 30}
print(z)
5
# intersection

k = x.intersection(y)
print(k)# {4, 5, 6}

# diffrence
k = x.difference(y)
print(k)# {1, 2, 3}
z = y.difference(x)
print(z)
print(len(z))
print(max(z))
print(min(z))
print(sum(z))
#pop,remove discard
x = {2,3,4}
# x.pop()# least value will be removed
# print(x)
x.remove(4)
print(x)

# discard: if element is there it will remove otherwise it won't riase error KeyError
x.discard(10)

x = frozenset()
print(type(x))
'''
'''
comprehensation
x = [1,2,3,4,5,6]

# [expression iteration]
y = [i*i for i in x]# [1, 4, 9, 16, 25, 36]
print(y)


z = []
for i in x:
    z.append(i*i)
print(z)

x = [1,2,3,4,5,6]
z = []
for i in x:
    if i%2==0:
        z.append(i)
print(z)

# [expression iteration condition]
print([i for i in x if i%2==0])

# [exression if else iteration]
print([i if i%2==0 else 0 for i in x])

# tuple
x = (1,2,3,4,5,6)
# [expression iteration condition]
print(tuple(i for i in x if i%2==0))

# [exression if else iteration]
print((tuple(i if i%2==0 else 0 for i in x)))

# set
x = {1,2,3,4,5,6}
# [expression iteration condition]
print({i for i in x if i%2==0})

# [exression if else iteration]
print({i if i%2==0 else 0 for i in x})

'''

#dict

x = {"a":123,"b":143,"c":153}
'''
for i,j in x.items():
    print(i,j)
'''

xx = {i:j*2 for i,j in x.items()}

print(xx)

zz = {i:j for i,j in x.items()if j%1==0}
print(zz)


zzz = {i:j if j%2==0 else 10 for i,j in x.items()} # {'a': 10, 'b': 10, 'c': 10}
print(zzz)






