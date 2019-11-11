#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#
class Solution(object):
    # def numDecodings(self, s):
    #     if not s:  #  or not s.isdigit()  # 不需要了. 循环里判断. 
    #         return 0
    #     N = len(s)
    #     f = [0] * (N + 1)  # 初始化
    #     f[0] = 1
    #     for i in xrange(N):
    #         if 0 < int(s[i]) <= 9:  # <=9 按照题意可以舍去
    #             f[i + 1] = f[i]
    #         # if i > 0 and 10 <= int(s[i-1:i+1]) <= 26:
    #         if i > 0 and 10 <= int(s[i - 1]+s[i]) <= 26:  # slice很慢.
    #             f[i + 1] +=+ f[i - 1]
    #         # if f[i + 1] == 0:  # early stopping加速
    #         #     return 0  
    #     return f[-1]

    def numDecodings(self, s):
        # f[i] = f[i - 1] + f[i - 2]
        pre2, pre1 = 1, 1  # pre1相当于-1, pre2 -2的位置.
        for i, char in enumerate(s):
            cur = 0  # 初始化啊..
            # Note 不能else return 0!!! 0可以用在构建10/20上..
            if 0 < int(char) <= 9:  
                cur = pre1
            # 忘记i>0, slice很慢                
            if i > 0 and 10 <= int(s[i-1]+s[i]) <= 26:  
                cur += pre2
            if cur == 0:  # 只有中间出现无法处理的0, 才会cur=0
                return 0
            pre2, pre1 = pre1, cur
        return cur  # 如果字符串为空, 还是需要额外判断

if __name__ == '__main__':
    """
    题设: 
        给定一个只包含数字的"非空"字符串，请计算解码方法的总数。
        A 1 Z 26
    TODO: 初始化两种方法, 选哪种???
    坑:  
        1. 不是dp[idx + 1] = dp[idx] +１!!
        2. 处理0的情况 '10' '01'. 并不是出现0就不对...
    解法1:
        DP数组之所以需要N+1, 是为了把0位置的判断也放进循环里.
        或者理解为空字符串有一种表达? 
    修改2: 
        不需要数组, 用两个变量代替. 
    修改3: early stopping
    """
    s = Solution()
    print(s.numDecodings('12'))
    print(s.numDecodings('99'))
    print(s.numDecodings('000123'))
    print(s.numDecodings('2267'))
    print(s.numDecodings('12'))
    print(s.numDecodings('226'))
    print(s.numDecodings('0'))
