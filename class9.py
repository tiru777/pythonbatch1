# Tuple

# immutable or it wont allow changebale
# indexing allow
# duplicates allow
# homogenous and hetrogeneous
# x = 1,
# x =()
# tuple keyword
# its a fixed length, we can't increase


#Methods

'''
- index
- count
- clear

'''
# functions: max,len,sum,min,sorted
'''

x = (1,2,3)
x[2]=20
print(x) # TypeError: 'tuple' object does not support item assignment
# indexing
x = (1,2,3,4,5)
print(x[2])# 3

x = (1,2,2,2,2,3,4,5)
print(x.count(2))
x = (1,2,3,4,5)
print(x.index(3))
x = (1,2,3,4,5,5,5,70,9801,2,3,4)
print(sorted(x))
print(max(x))
print(min(x))
print(len(x))
print(sum(x))

x = (1,2,3,4,5,5,5,70,9801,2,3,4)
z =0
for i in x:
    z = z+i
print(z)

'''



























