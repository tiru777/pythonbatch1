def func_even_odd(value):  # 5
    """

    :param value: integer or float
    :return: check even or odd
    """
    if value % 2 == 0:  # 5%2 1==0
        return f"{value} is even"
    else:
        return f"{value} is odd"


# i = input("enter the value:") # 5
# data = func_even_odd(int(i))
# print("output is :", data)


# reverse the string
def reverse_string(str_name):  # "vinod kumar"
    # return str_name[::-1]
    name = ""
    for i in str_name:  # vinod
        name = i + name  # iv
    return name


#
# data = reverse_string("vinod kumar")
# print(data)


def count_occuranece(data):
    dictt = {}
    for i in data:
        dictt[i] = data.count(i)
    return dictt


# count_occuranece([11,1,1,1,1,1,1,2,2,2,3,3,3,4])


# lambda
'''
# no need to mention return keyword, it will take care of returning the output
syntax:
    lambda arguments: expression (parameters)
    variable = lambda arguments: expression
    print(variable(parameters))

'''
def reverse_st(str_name):  # "vinod kumar"
    return str_name[::-1]


# print(reverse_st("vinod"))


x = (lambda x: x[::-1])("vinod")
# print(x)
xx = lambda x, y: x / y
# print(xx(20,10))

y = lambda *args: (i * i for i in args)
# print(list(y(1, 2, 3, 4, 5)))

# print(list((lambda *args: (i * i for i in args))(1, 2, 3, 4, 5)))

# generators
# iterators
# decorators


# generators:
'''   It is a function which uses yield keyword to return 
        the iteration data in the form of generator object
        return:
          - it will only return first iteration of sequence data 
        yield:
            - it will yield all iteration until completion of sequence data
        '''
def func_name(*args):
    for i in args:
        print(i)

def func_namee(*args):
    for i in args:
        return i

def func_name_gen(*args):
    for i in args:
        yield i


vv = func_name_gen(1,2,3,4,5) # <generator object func_name_gen at 0x0000022F5AEA5D20>
# print(list(vv))
# for j in vv:
#     print(j)

# iterator
"""
It is used for iterating the sequence of elements using iter keyword and next
- '__iter__' already present in the for loop, most of the requirements for loop only full fill this iterations
"""

def func():
    """

    :return: return elements
    """
    for i in "thirumala":
        print(i)
        print(dir(i)) # '__iter__'

# print(func())
# print(func.__doc__) # :return: return elements
xxx = [10,20,30,40]
data = iter(xxx)
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))


# decorators
"""
- decorator is a top of the function
decorator is a function which will take function as argument, without distrubing existing function
we can add features to the function
"""
# nested functions
def func_name_inner():
    def inner_func():
        return "i am from inner function"

    vv = inner_func()
    print("inner function o/p:",vv)

    return "i am from main function"


# print(func_name_inner())


# nested functions
def func_name_innerr():
    def inner_func():
        return "i am from inner function"
    vvvv = inner_func()


    return vvvv


# vvv = func_name_innerr()
# print(vvv)

def func_name_innerrr():
    def inner_func():
        return "i am from inner function"

    return inner_func()


vvv = func_name_innerrr()
# print(vvv)







def dec_ch(func):
    print("i am from decorator")
    return func

@dec_ch
def funcc():
    return "i am from main function"

# print(funcc())


'''def dec_check2(func):
    def inner():
        return "i am from decorator inner two"
    return inner

@dec_check2
def funcc_main():
    return "i am from main function"

print(funcc_main())
'''
def dec_check2(func):
    def inner(arg1,arg2):# 10,2
        if arg1>arg2: #10>2
            return func(arg1,arg2)# 5
        else:
            return f"{arg1} is less than {arg2}"

    return inner #5

@dec_check2 #5
def funcc_main(arg1,arg2):
    return arg1/arg2

# print(funcc_main(10,2)) # 5

print(funcc_main(22,40)) # 5
















