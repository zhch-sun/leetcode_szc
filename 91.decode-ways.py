#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#
class Solution(object):
    # def numDecodings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     if not s:
    #         return 0
    #     dp = [0] * (len(s) + 1)
    #     dp[0] = 1  # 这个初始化...
    #     dp[1] = 1 if s[0] != '0' else 0
    #     for idx in range(1, len(s)):  # the index of s
    #         p1 = int(s[idx])
    #         p2 = int(s[idx-1: idx+1])  # 这个奇怪的slice. 
    #         if 0 < p1 <= 9:  # 注意符号.. 另外这里不需要 <=9..
    #             # 因为dp[idx+1]本身是0, 所以如果出现连续两个dp为0, 后面必为0
    #             dp[idx + 1] += dp[idx] 
    #         if 10 <= p2 <= 26:
    #             dp[idx + 1] += dp[idx - 1]
    #     return dp[-1]
        
    def numDecodings(self, s):
        # 必须要把cover所有len(s) == 1的跳出条件, 因为这时候cur没有...
        if not s or s == '0':
            return 0
        if len(s) == 1:
            return 1
        pre2 = 1
        pre1 = 1 if s[0] != '0' else 0
        for idx in range(1, len(s)):  # the index of s
            p1 = int(s[idx])
            p2 = int(s[idx-1: idx+1])  # 这个奇怪的slice. 
            cur = 0
            if 0 < p1 <= 9:
                cur += pre1
            if 10 <= p2 <= 26:
                cur += pre2
            pre2 = pre1
            pre1 = cur
        return cur    


if __name__ == '__main__':
    """
    这个dp并不简单! 注意 string中可能有若干个0.
    1. 不是dp[idx + 1] = dp[idx] +１!!
    2. 处理0的情况 '10' '01'
    3. 初始化dp[0]是为了递推的正确性. 否则只能dp[idx + 1] += dp[idx - 1]在这个后面加一个判断..
    解法2: 因为只依赖前两个值, 所以也可以不需要整个dp[]
    解法3: 用乘法代替里面的两个if判断, 用python的交换赋值代替后面的赋值, 这样for循环里可以缩成一句话..
    """
    s = Solution()
    print(s.numDecodings('99'))
    print(s.numDecodings('000123'))
    print(s.numDecodings('2267'))
    print(s.numDecodings('12'))
    print(s.numDecodings('226'))
    print(s.numDecodings('0'))
