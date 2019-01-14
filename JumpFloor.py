##  斐波那契数列  ##

def jump(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return jump(n-1) + jump(n-2)

for i in range(1,10):
    print (jump(i))            #  1,1,2,3,5,8,13,21,34


##  跳台阶问题(1) ##
'''
青蛙一次可以跳1级，也可以跳2级  
F(n) = F(n-1) + F(n-2)
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
    

##  跳台阶问题(2) ##
'''
该青蛙可以跳1,2,3,...,m-1,m级,台阶一共 n 级
f(n) = f(n-1) + f(n-2) + f(n-3) + ... + f(n-(m-1)) + f(n-m)
f(n-1) = f(n-2) + f(n-3) + f(n-4) + ... + f(n-m) + f(n-m-1)

上下相减： f(n) = 2*f(n-1) - f(n-m-1)

当 m = 2 时，1,2,3,5,8,13   和上面的一样
当 m = n 时，注释掉前三行就可以了 

'''

def jumpnji(n):
    m = 2
    if n > m:
        return 2*jumpnji(n-1) - jumpnji(n-1-m)
    if n <= 1:
        return 1
    else:
        return 2 * jumpnji(n-1)

# 1,2,3,5,8,13
for i in range(1,7):
    print (jumpnji(i))













