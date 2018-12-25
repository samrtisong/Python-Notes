
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

# (3) 数组之和为S的两个数--剑指offer
n=6
num=[]
minin=12
s=[1,2,3,4,5]
ss=[]
sss=[]
s6=[]
for i in range(len(s)):
	for j in range(i+1,len(s)):
		ss.append(s[i])
		ss.append(s[j])
print ss
for i in range(0,len(ss),2):
	a = ss[i]+ss[i+1]
	if a==n:
		sss.append(ss[i])
		sss.append(ss[i+1])
print sss
if len(sss)==0:
	print sss
else:
	minin=sss[0]*sss[1]
	for i in range(0,len(sss),2):
		b=sss[i]*sss[i+1]
		print b
		if b<=minin:
		minin=b
		s4=sss[i]
		s5=sss[i+1]
	s6.append(s4)
	s6.append(s5)				
	print s6

