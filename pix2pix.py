
# 字符串处理 #
# （1）输出子字符串
tinput='abc'
output=[]
for i in range(0,len(tinput)):
    for j in range(i+1,len(tinput)+1):
		output.append(tinput[i:j])
print output                          # ['a', 'ab', 'abc', 'b', 'bc', 'c']

# (2) 字符串的切割和拼接 ---剑指 翻转单词顺序列

s = "wei liu song"
b=s.split(' ')
a=s.split(' ')
print b            # ['wei', 'liu', 'song']
print ' '.join(b[::-1])  # song liu wei

for i in range(len(b)):
	a[2-i]=b[i]
print ' '.join(a)        # song liu wei

# (3) 字符串异常处理
try:                      # 判断字符串s是否是数值型字符串 ---剑指
	float(s)          # 检测是否有异常
	return True
except:
	return False      # 上述异常发生时执行





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

# (4)数组倒序输出的几种方法
a=[1,2,3,4,5]
b=[]
for i in a:
	b.insert(0,i)   # method-1 使用函数insert(index, element)
	print b
print b

print a[::-1]       # method-2
























