#
# @lc app=leetcode id=309 lang=python
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution(object):
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     N = len(prices)
    #     if N < 2:
    #         return 0
    #     f = [[0, float('-inf')] for _ in xrange(N + 2)]
    #     for i in xrange(2, N + 2):
    #         f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i-2])
    #         f[i][1] = max(f[i-1][1], f[i-2][0] - prices[i-2])  # 减号!
    #     return f[-1][0]

    def maxProfit(self, prices):
        sold, pre_sold = 0, 0
        hold = float('-inf')
        for n in prices:
            hold = max(hold, pre_sold - n)
            pre_sold = sold
            sold = max(sold, hold + n)
        return sold

if __name__ == '__main__':
    """
    解法1:
        f[i][0] = max(f[i-1][0], f[i-1][1] + prices[i])
        f[i][1] = max(f[i-1][1], f[i-2][0] - prices[i])
        分析 见123题
        其实dp就是记录前i个的状态机
    解法2:
        状态机, 三个转移方式sell buy rest 三个状态hold sold pre_sold
        hold = max(hold, pre_sold - prices[i])
        pre_sold = sold
        sold = max(sold, hold + prices[i])  # 两个来源rest 和 sell
    """
    s = Solution()
    print(s.maxProfit([1,2,3,0,2]))
        
# @lc code=end

