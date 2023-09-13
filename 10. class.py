# dict
# it is key value pair, pair separted by comma
  #key
    # where keys are immutable,
    #it won't allow duplicates keys,
    #it is unique,
    #keys are int,float,str
    # homogenous and hetrogenous
   # values
    # values mutable
    # it will allow duplicate values
    # homogenous and hetrogenous values it will allow [int,str,float]
    # list,dict,set,int,float,str
# {'a':10,'b':20.2,1:20,12.1:2}
#empty dict
    #x= {} or dict()

'''
# adding
x = {'a':10,'b':20}
x['c']=30
print(x)

# update
y = {'d':20,'e':40,'f':10}
x.update(y)
print(x)

# key and values
print(x.keys())
print(x.values())
print(x.get('e'))

# items
print(x.items())
# remove
x.pop('e')
print(x)
x.popitem()
print(x)
x.clear()
print(x)
'''
'''
y = {'d':20,'e':40,'f':10}

for key,value in y.items():#[('d',20),()]
    print("key is:",key)
    print("value is:",value)
'''
'''
y = {'d':20,'e':10,'f':10}

for key,value in y.items():
    if value>10:
        y[key]=value+10
print(y)
'''
'''
x = input("enter the password:")
for key,value in y.items():
    if x in y.values():
        print("you got access")
print(y)

'''
y = {'d':20,'e':10,'f':10}
print((tuple(y.items()))[2])














