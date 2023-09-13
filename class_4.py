# conditions

#if, else, elif, if elif else
x = 20
y = 30
z = 20

'''
if True:
    print("hey you came to if block")
'''

'''
if (x>y):# whenever if condition satisfy then only it will goto inside block
    print("x is greter than y")
'''

'''
if (x>y):# whenever if condition satisfy then only it will goto inside block
    print("x is greter than y")
else:
    print("x is less than y")
'''
'''
if (x>y):# whenever if condition satisfy then only it will goto inside block
    print("x is greter than y")
    
elif y<z:#30<20
    print("y is less than z")

else:
    print("y is greter than x and z")

'''
'''
if (x>y):#20>30
    print("x is greter than y")
    
elif y<z:#30<20
    print("y is less than z")

elif x<z:#20<20
    print("y is less than z")

else:
    print("y is greter than x and z")

'''





"""
x = input("enter the name:")# reddy
y = input("enter any word:")#d
if y in x:# d in reddy
    print(f"{y} in {x}") # d in reddy
else:
    print("{y} not in {x}")

"""

x = int(input("enter the x value:"))#10
y = int(input("enter the y value:"))#20
z = int(input("enter the z value:"))#30

if x>y and y<z:#10>20 and 20<30
    print(" i came to if block")

elif x<y or y>z:#10<20 or 20>30 #True or False
    print("i came to elif block")

else:
    
    if x<z:
        print("i came to else block")


















    
    
