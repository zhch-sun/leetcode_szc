#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        
if __name__ == '__main__':
    """
    这道题不能用之前的Kadane's Algorithm的trick
    General k交易 DP解法: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39608/A-clean-DP-solution-which-generalizes-to-k-transactions
    当前时步最大值为前一个时步最大值和以当前时步为最后一个卖出的最大值. 
    当前时步最后卖出的最大值是 当前时步的盈利加上 以上一个时步结束的最大值或上一个时步结束且少一个交易的最大值
    这里有一个https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution
    推出最简单dp的方法. 
    和188实际是一道题, 而且123和188实际还有更快解法....
    """
    s = Solution()

