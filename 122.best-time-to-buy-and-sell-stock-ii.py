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
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i-1], 0)
        return res

if __name__ == '__main__':
    """
    understand the peak and valey
    """
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))

