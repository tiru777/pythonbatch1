# string manipulation, math, indexing
'''


x = "vinodkumar"

# upper and lower
y = x.upper() #VINOD
# print("lower to upper:",y)
xx = y.lower()
# print("lower convertion from upper",xx)


# checking lower or upper
# print(xx.islower())
# print(y.isupper())

#replace
#str.replace("old","new")
z = x.replace("kumar","Reddy")
# print(z)

#title
print(x.title())# Vinod Kumar

# capitilze
print(x.capitalize())

# split
print(x.split())
# print(x.split("d"))# based on this element will split and it wont apper in list

# endswith # checking elements ends with or not and it will return True or False
print(x.endswith('d'))
print(x.startswith('v'))

# length
print(len(x))

# join
print("".join(x))# how to join two strings without spaces
print(x.join("reddy"))


import math
# print(help(math))
print("ceil",math.ceil(24.3))# 25

print("floor",math.floor(24.3))# 24 

print("floor",math.floor(24.3))# 24

'''


x = "vinodkumar"
'''
# print("3 rd index",x[3])#o
#print("7 th index",x[7])#m
#print("-3 index",x[-3])#m
# print("-5 index",x[-5])#k

#str[start:stop] #stop-1 print
#print(x[3:7])#odku
# print(x[6:8])#um

#print(x[-6:-2])# in negitive index we have to start with minimum

# str[start:stop:step]
# print(x[2:7:2])# ndu

print(x[2:])# nodkumar
print(x[:6])# vinodk
print(x[::2])#vndua
'''
x = "vinodkumar"
print(x[2:8])#nodkum
print(x[2:8:1])#nodkum
print(x[::-1])#ramukdoniv # how to reverse the string
def fun(strr):
    print("hellow world",strr)

print(fun("thiru"))