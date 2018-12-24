
# 字符串处理 #
# （1）输出子字符串
tinput='abc'
output=[]
for i in range(0,len(tinput)):
    for j in range(i+1,len(tinput)+1):
		output.append(tinput[i:j])
print output                          # ['a', 'ab', 'abc', 'b', 'bc', 'c']

# (2) 





# 数组处理
# （1）数组排序
input = [2,1,5,4,3]
b=sorted(input)
print b        # [1, 2, 3, 4, 5]

input.sort()
print input    # [1, 2, 3, 4, 5]

# (2) 连续子数组的最大和---剑指offer
array=[-1,-2,-3,-4,-5]
maxnum = array[0]
curnum = array[0]
        
for i in array[1:]:
    if curnum <=0:
        curnum = i
    else:
        curnum += i
    if curnum > maxnum:
        maxnum = curnum
print maxnum

