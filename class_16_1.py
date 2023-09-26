"""
# specific function import from specfic module
# syntax
    - from module import func_name
    - only you can call the specfic function which you imported

from class_15 import func_name_t
da = func_name_t()


"""
"""
# we can import all variables and functions, classes in respective module by using *
# syntax
    - from module_name import *
    - calling: func_name()
    
from class_15 import *  
data = func_name_t(20)
print(list(data))

d = func_name_tiru(10)
print(list(d))


"""
"""
# import specific module
# syntax
    - import module_name
    - module_name.function_name()

import class_15

data = class_15.func_name_t(20)
print(list(data))

d = class_15.func_name_tiru(10)
print(list(d))

"""

"""
Packages: whenever multiple modules and __init__.py is there, then it will act as package
library: package is nothing but one library, we use this package in any module. 
        - either single package or multiple packages  is called as library
module: .py extension available is called as module
# syntax
    - from package.module import * 
    - from package.module import func_name

from class_16.test2 import func_name_test


data = func_name_test(10,20,30,40)
print(data)
"""
"""# as alias from renaming

from class_16 import func_name_test as fp
da = fp(1,2,3,4)
print(da)"""

