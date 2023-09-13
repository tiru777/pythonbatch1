# input keyword from python is using for taking values from enduser
#print formats,math
# operators
'''

+,-,/,//(floor division),*,**,%

a = 17
b = 3
z = a+b #50
print("sum operator +",z)
y = a-b
print("diffrence -",y)
kk = a/b #
print("divide /",kk)
#floor division
zz = a//b
print("floor division //",zz)
cc = a*b
print("multiplication *",cc)
vv = a**b
print("power of **",vv)# 2 ^3

ccc = a%b #17 we are going divide by 3 and we will get reminder 2
print("modulo of %",ccc) # it wont divide it will take reminder value while dividing two values

'''

'''
==,!=,
a = 10
b = 20
print("equal operator:",a==b)
print("not equal operator:",a!=b)# not qual to

'''
'''
>,<,>=,<=,
a = 20
b = 30
print("greter than operator",a>b)#False
print("less than operator",a<b)# True
print("greter than equal to",a>=b)# False
print("less than are equal to",a<=b)#True
'''
'''
and,or,not
and: Both condition must be true ==>&
or: any one condition True  => |
not: ~

x = 30
y = 20
z = 10

print("and",x>y and y<z) # x>y True and False ==>True and False ==> False
print("or",x>y or y<z) # x>y True or False ==>True or False ==> True
print("not",not x>y) # False

print("and",(x>y) &(y<z)) # x>y True and False ==>True and False ==> False
print("or",(x>y)|(y<z)) # x>y True or False ==>True or False ==> True
print("not",~(x>y))

# 1 True
# 0 False

print("using numbers and",1 and 0)
print("using numbers and",1 and 1)
print("using numbers or",1 or 0)
print("using numbers or",1 or 1)

'''

"""
Membership Operator
in : it will check if value present in any collection or string
not in: it will check if value not present in any collection or string

x = "thirumala reddy"
print("h" in x)# True
print("z" in x) # False

print("h" not in x) #False
print("z" not in x)# True
"""

"""
Identity Operators
when values assigned with same refrenced objects then only id will be same
is:
is not

x = 20
y = 30
print("x  id is",id(x))
print("y id is",id(y))

print("is identity:",x is y)
print("is not identity:",x is not y)
z = 20
zz = 20
print("z  id is",id(z))
print("zz id is",id(zz))
print("is identity:",z is zz)
print("is not identity:",z is not zz)
"""

"""
Incremental operator
x = 10
x = x+1 #11
x = x-1 #9

x+=1#11
x-=1#9
"""

"""
# input
# data we are going to take from enduser

# taking string from user
x = input("enter the value:")#str #40
#print(type(x))#<class str>
zz = int(x)#str==>int
print(zz+50)#int+int #40+50=>90

# taking string and directly converting to int
x = int(input("enter the values:"))# direct #20
print(x+20)

x = int(input("enter x value:"))#10
y = int(input("enter y value:"))#2
z = int(input("enter z value:"))#5

print(x+y+z)#17
print(x>y and y<z)#True and True ==>True

x = input("enter x value:")# chanikya
xx = input("enter x value:")# reddy

print(x+xx)#str+str => chanikyareddy

x = input()
print(x)
"""
#str =>%s
#int =>%d

""" format strings
x = input("enter the course name:")
y = int(input("enter course duration:"))

print("He is learning {} course".format(x))

print(f"he is learning {x} course in days {y}")

print("He is learning %s course in some days %d"%(x,y))
"""
# added comment















































