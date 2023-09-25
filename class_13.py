# function
#  repeatable code minimize  --->DRY(don't repeat yourself)
# they are two types of functions
# predefined functions: print,len,min,max,sum,sorted,etc
# user defined functions: Customizing of our requirement by using def keyword

# bare function
def func_name():
    """
    This function returning hellow world string
    :return: hellow world
    """
    print("hellow world")


# func_name()  # function calling

def fun_name():
    """
    This function returning hellow world string
    :return: hellow world
    """
    return "hellow world i am from class 13 python file"


# vv = fun_name()  # function calling
# print(vv)

def position_args_fun(arg1, arg2):  # 10,20
    """
    positional arguments: whatever arguments defined same position only we should pass values
    :param arg1: value either int or float
    :param arg2: value either int or float
    :return: multiplication of arg1 and arg2
    """
    x = arg1 * arg2  # 10*20 =200
    return x  # 200


# v = position_args_fun(10,20) #200
# print("function output",v)

def keyword_args_fun(arg1, arg2):  # 10,20
    """
    keyword arguments: whatever arguments defined we should pass along with key and value
    :param arg1: value either int or float
    :param arg2: value either int or float
    :return: multiplication of arg1 and arg2
    """
    print("argument 1 value:", arg1)
    print("argument 2 value:", arg2)

    x = arg1 * arg2  # 10*20 =200
    return x  # 200


# v = keyword_args_fun(arg2=10,arg1=20) #200
# print("function output",v)


def default_args_fun(arg1, arg2=30):  # 10,20
    """
    default arguments: whatever arguments defined we should pass otherwise default values it wil use
    :param arg1: value either int or float
    :param arg2: value either int or float
    :return: multiplication of arg1 and arg2
    """
    print("argument 1 value:", arg1)
    print("argument 2 value:", arg2)

    x = arg1 * arg2  # 10*20 =200
    return x  # 200


# v = default_args_fun(10,20) #200
# print("function output",v)
# v = default_args_fun(10) #300
# print("function output",v)
# v = default_args_fun() #300
# print("function output",v)


def variable_length_or_annonmays(*args):
    """
    aany number of sequence values we can pass by mentioning * args
    :param args: sequence
    :return: args
    """
    return args


# print(variable_length_or_annonmays(1,2,3,4,4,5,6))

def variable_length(*args):
    """

    :param args:
    :return: square
    """
    x = []
    for i in args:
        x.append(i * i)

    return tuple(x)


# print(variable_length(1,2,3,4,4,5,6)) # [1, 4, 9, 16, 16, 25, 36]


def variable_length_or_keyword(**kwargs):
    """
    any number of sequence key values we can pass by mentioning **kwargs
    :param kwargs: sequence
    :return: dictionary
    """
    return kwargs


# print(variable_length_or_keyword(a=20,b=30,c=40,d=90))# {'a': 20, 'b': 30, 'c': 40, 'd': 90}

def variable_length_or_key(**kwargs):
    """
    any number of sequence key values we can pass by mentioning **kwargs
    :param kwargs: sequence
    :return: dictionary
    """
    d = {}
    for key, value in kwargs.items():
        d[key] = value * 2
    return d


# print(variable_length_or_key(a=20,b=30,c=40,d=90)) # {'a': 40, 'b': 60, 'c': 80, 'd': 180}

def both_args_kwargs(*args, **kwargs):
    x = []
    d = {}

    for i in args: x.append(i * i)

    for key, value in kwargs.items(): d[key] = value * 2

    return x, d


v = both_args_kwargs(1, 2, 3, 4, 5, a=20, b=30, c=40, d=90)


# print(v) # ([1, 4, 9, 16, 25], {'a': 40, 'b': 60, 'c': 80, 'd': 180})


