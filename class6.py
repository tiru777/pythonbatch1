# loops
    # for
        #break
        #continue
    # while
        # break: whenever condition satisfy it will break the loop
        # continue: whenever condition satisfy it will pass to next iteration
#for else
    # whenever for iteration completely done then only else block will execute
#for break else
    # whenever for iteration satisfy the condition it will break
        # the loop and it won't go for the else block
    
        
#range
#range(stop)
#range(start,stop)
#range(start,stop,step)
#range(stop,step)

'''

print(list(range(10)))# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10))) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2)))# [1, 3, 5, 7, 9]
print(list(range(-10,0,1)))#[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

print(list(range(-10,-20,-1)))# [-10, -11, -12, -13, -14, -15, -16, -17, -18, -19]
'''


"""
for variable in sequence:
    print(variable)

x = "Thirumalareddy"

for name in x:#Thirumalareddy
    print(name)# t

y = range(10)
for i in y:
    print(i)

for k in range(5,10):
    print(k)#

for i in range(10):
    if i==5:
        print(i-2)#3
        print(i**2)# 25
for j in "vinodkumar":
    if j == "d":
        print(j+"vinod")

for j in range(10):
    if j!=5:
        print(j)
for i in range(10):
    if i == 5:
        break
    print(i)
for k in 'vinodkumar':
    if k=='o':
        break
    print(k)

for j in range(10):
    if j ==6:
        continue
    print(j)
    
"""
for i in range(10):

    print(i)
else:
    print("thirumala")

for i in range(10):
    if i ==5:
        break
else:
    print("thirumala")






































