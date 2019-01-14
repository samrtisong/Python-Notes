##  斐波那契数列  ##

def jump(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return jump(n-1) + jump(n-2)

for i in range(1,10):
    print (jump(i))            #  1,1,2,3,5,8,13,21,34


##  跳台阶 ##
'''
青蛙一次可以跳1级，也可以跳2级
counter = 3     # 1,1,2,3,5,8  
counter = 2     # 1,2,3,5,8,13
'''

def jumpfloor(n):
    if n == 0:
        return 0
    elif n <= 1:
        return 1
    i1, i2 = 1,1
    counter = 2
    while counter<=n:
        temp = i1+i2
        i1 = i2
        i2 = temp
        counter += 1
    return i2
for i in range(1,7):
    print (jumpfloor(i))


