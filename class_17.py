# Regular Expression
"""
finding the pattern(string or numbers) in raw string
Methods:
    - match: it will match first pattern in starts of the string
    - search: it will search return single matched pattern in entire string
    - findall: it will return all matched patterns in the string
    - sub: whenever matches it will substitute the pattern
    - split: whenever pattern matches it will split
---
[0-9] --> it will return single matched number
\d --> it will return single matched number
[a-zA-Z] --> it will return single matched charector
\w --> it will return single matched charectr [a-zA-Z0-9]
^ --> it is used for start of the string
$ --> it is used for end of the pattern
{} --> {1,} how many charectors or numbers present in string
. --> single charector return
\s --> single space
* --> 0 or more occurances
+ --> 1 or more occurences

"""
import re

# match
'''
re.match('pattern',string)

xx = "hellow i am the stirng hellow hellow"
data = re.match('hellow', xx)  # it will only check the pattern in start of the string
print("match method:",data.group())
'''


# search
"""
re.search('pattern',string)

xx = "i am the stirng hellow hellow"
data_search = re.search('hellow',xx)
# it will check the pattern in either start or end or middle of the single pattern in string
print("search method:",data_search.group())

"""


# findall
"""
re.findall("pattern",str)

xx = "i am the stirng hellow hellow"
data_find = re.findall('hellow',xx)
# it will check the pattern in either start or end or middle of the single pattern in string
print("findall method:",data_find)
"""



# subst
"""
re.sub("pattern","replace",str)

xx = "i am the stirng hellow hellow"
data_sub = re.sub("hellow","reddy",xx)
print("sub method:",data_sub)

"""


# split
"""
re.split("pattern",str)

xx = "i am the stirng hellow hellow"
data_split = re.split("h",xx)
print("split method:",data_split)
"""


xx = "hel1low i am the hellow3 helilow hellow1 2 3 4"

# d = re.findall("^hellow",xx)
# dd = re.findall("w$",xx)

# d = re.findall("hellow [a-zA-Z]",xx)
# d = re.findall("hellow\d", xx)
# dd = re.findall("\d",xx)
# d = re.findall("i",xx)
dd = re.findall("hel\w{1,3}",xx) # ['hel1lo', 'hellow', 'helilo', 'hellow']
d = re.findall("hel\w*",xx) # ['hel1low', 'hellow3', 'helilow', 'hellow1']
d = re.findall("hel\w+",xx) # ['hel1low', 'hellow3', 'helilow', 'hellow1']

print(dd)











# Example for file reading with regax
"""
with open("file.txt",'r') as fp:
    data = fp.read()
    data_find = re.findall("aadhar number",data)
    print(data_find)
"""



