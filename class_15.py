# Exceptional handling
# whenever error raises in code interpreter abnormally terminates the script

"""

# try-except
    # you can use try and except blocks for handling the error
        - whenever error found in try block interpretor checks whether it has error handlings are there not
        - if handling are there it will got to except block and it will execute
# try-except-finally
    - finally
        - whenever error raised in try block or not it will execute in finally block code
        - ex: database connection close
# raise
    - you are raising the error explictly  by using raise keyword
    - raise "error /Name"
# try -except-else:
    # else block: whenever they is no error found in try block then only it will execute
try:
"""

"""
# try-except
try:
    for i in range(10):
        print(i)
except:
    print("error found in try block")

"""
"""
# try-except: if you know already which error found in try block use Error in Exception
try:
    x = (1, 2, 3, 4)
    x[2] = 40  # assignment error
except TypeError:
    print("hey you got Type error")
"""
"""
# try-except: if you dont know which error find
try:
    x = (1, 2, 3, 4)
    x[2] = 40  # assignment error
except Exception as error:
    print("hey you got Type error",error)
"""

"""
# try-except-finally:
try: 
    for i in range(10):
        print(i)
except:
    print("error is found")
finally:
    print("i am from finally block")
"""
# example
"""

try:

    x = (1, 2, 3, 4)
    x[2] = 40  # assignment error
    d = {"a": 20, "b": 40}
    d.pop('c')
    print(x)
    print("hellow worlf")
except TypeError:
    print("hey you got type error please cross check")

except Exception as er:
    print("error is:", er)
except:
    print("error found code")
finally:
    # finally block it will execute whenever error raises or not
    print("helle i am from finally")
"""

# raise
"""try:
    for i in range(10):
        print(i)
    raise "TypeError"
except TypeError:
    print("hey i got type error")"""

# try -except-else:
# else block: whenever they is no error found in try block then only it will execute
try:
    def func_name_tiru(x):
        for i in range(2, x):
            yield i * i

except TypeError:
    print("specific error you can handle")

except Exception as error:
    print("when you don't know error is ", error)

except:
    print("error found")

else:
    print("else: when they is o error it will execute")

finally:
    print("finally: error raised or not it will execute")

# print(list(func_name_tiru(10)))


try:
    def func_name_t(x):
        for i in range(2, x):
            yield i * i

except Exception as error:
    print("when you don't know error is ", error)
