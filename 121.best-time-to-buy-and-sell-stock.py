#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
class Solution(object):
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     n = len(prices)
    #     if n < 2:
    #         return 0
    #     dp = [0] * n
    #     mini = prices[0]
    #     for i, p in enumerate(prices[1:]):  # pos = i + 1
    #         dp[i+1] = max(p - mini, dp[i])
    #         mini = min(mini, p)
    #     return dp[-1]

    def maxProfit(self, prices):
        # 实际上是转换成为一个差值序列, 求最大连续子序列.
        n = len(prices)
        local_max = global_max = 0
        # if n < 2:
        #     return 0
        for i in xrange(1, len(prices)) :
            local_max = max(local_max + prices[i] - prices[i-1], 0)
            global_max = max(local_max, global_max)
        return global_max


if __name__ == '__main__':
    """
    my own algorithm record a minimum price. 
    也可以用max subarray的Kadane's Algorithm求最大连续子序列. 
    """
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
