
（1）#  正则表达式匹配 #















(2) # 求1+2+3+4+5+...+n 

class Solution:
    def Sum_Solution(self, n):
        # write code here
        # reduce 函数
        return reduce(lambda item1, item2: item1+item2, range(n+1))
        # 递归
        if n==1:
            return 1
        return self.Sum_Solution(n-1)+n


