#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(1, len(prices)):  # max很优雅
            res += max(prices[i] - prices[i-1], 0)
        return res

if __name__ == '__main__':
    """
    题设: 可以进行无穷次交易, 最大收入.
    解法: greedy, 只有上边沿赚钱. 
    """
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))

