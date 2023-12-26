#
# @lc app=leetcode id=714 lang=python
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        s, h = 0, float('-inf')
        s1, h1 = 0, float('-inf')
        for n in prices:
            s = max(s1, h1 + n)
            h = max(h1, s1 - n - fee)
            s1, h1 = s, h
        return s

if __name__ == '__main__':
    """
    直接状态机
    两种状态, sold hold, 三种动作, rest, sell, buy
    需要保存之前的状态
    s = max(s, h + n)
    h = max(h, s - n - fee)
    """
    s = Solution()
    print(s.maxProfit([1, 3, 2, 8, 4, 9], 2))
        
# @lc code=end

