# Tuple

# immutable or it wont allow changebale
# indexing allow
# duplicates allow
# homogenous and hetrogeneous
# x = 1,
# x =()
# tuple keyword
# its a fixed length, we can't increase


#Methods

'''
- index
- count
- clear

'''
# functions: max,len,sum,min,sorted
'''

x = (1,2,3)
x[2]=20
print(x) # TypeError: 'tuple' object does not support item assignment
# indexing
x = (1,2,3,4,5)
print(x[2])# 3

x = (1,2,2,2,2,3,4,5)
print(x.count(2))
x = (1,2,3,4,5)
print(x.index(3))
x = (1,2,3,4,5,5,5,70,9801,2,3,4)
print(sorted(x))
print(max(x))
print(min(x))
print(len(x))
print(sum(x))

x = (1,2,3,4,5,5,5,70,9801,2,3,4)
z =0
for i in x:
    z = z+i
print(z)

'''

'''
Linux

ls : list of items in the current folder
ls -a: list of items and hidden items in the current folder
cd : change directory
pwd : present working directory
mkdir :create new directory
rmdir :remove directory(folder)
chdir :change directory
rm :remove file or folder ex:rm *.jpg removes all jpg files
*  wild card
mv :move or rename a file or folder to a new location
Note :study move syntax
touch :creating new file ex:touch file.txt
cat : display the file content ex:cat file.txt
less : display portion of a file and file content
curl :used for file transfer
clear : clear in terminal
'''

























