
'''
# print
# print()
print("hellow world")
#hellow world
print(10)
#10
print(1.1)
#1.1
print(True)
#True
print("hello world has a number:",7)
#hello world has a number: 7

#concatination
print(10+10)# int+int
print(1.1+1.1)#float+float
print("name"+"vinod")#str+str
#int+str
print(str(1)+"strrrr")



'''

# python
'''python is interpter scripting lang,
       is dynamic programming lang(no need mention any datatype explicetly)
       is functional based (def )
       is object oriented(class )
       is high levelprogramming lang
'''
"""
# python Keywords
import os,sys,keyword
print(keyword.kwlist)
#print("path",sys.path)
#print(os.getcwd())

keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# present keywords 35 in python
"""











# variables

'''
int, float, string boolean(true or false)

# int
x = 10
print("number is int",x)
print("type is",type(x))

#float
y = 1.1
print(y)
print(type(y))

#string
x  = 'thirumala reddy'
print(x)
print(type(x))

y = "vinod"
print(y,type(y))

zz = """chanikya"""
print(zz,type(zz))

#z = """bhargav"""# we can write single triple quoatations also
print(z,type(z))

#bool
z = True
print(z,type(z))

y = False
print(y,type(y))

x = 20
y = 20
print(x==y)
'''
# type casting or convertion
'''
int==>float
float==>int

x = 20
print("x is ",x,type(x))# x is  20 <class 'int'>
y = float(x)
print("y is ",y,type(y))#y is  20.0 <class 'float'>

int ==>str
str ==>int
x = 20
print(x,"x type is",type(x))# 20 x type is <class 'int'>
y = str(x)

print(y,"y type is",type(y))#20 y type is <class 'str'>

float ==>str
str ==>float

x = 20.1
print(x,"x is type",type(x))# 20.1 x is type <class 'float'>
z = str(x)#'20.1'
print(z,"z is type",type(z))#<class 'str'>
yy = float(z)
print(yy)# 20.1

#str(float)=>int
# string decimal values('20.1'),its not possible to convert directly to int(20),
# we have to convert string decimal to float(20.1) then convert int(20)
zz = float(z)
yy = int(zz)
print(yy)


# operators
'''
'''
+,-,/,//(floor division),*,==,!=,>,<,>=,<=,and,or,not

'''

"""
x = 4
y = 3

print("sum",x+y)

"""