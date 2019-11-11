#
# @lc app=leetcode id=188 lang=python
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start

import heapq
class Solution(object):
    # def maxProfit(self, k, prices):
    #     """
    #     :type k: int
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     N = len(prices)  # 处理特殊值.
    #     if k >= N // 2:  # 需要判断, 尤其c里面
    #         res = 0
    #         for i in xrange(1, len(prices)):  # max很优雅
    #             res += max(prices[i] - prices[i-1], 0)
    #         return res

    #     stack = []
    #     profits = []
    #     i = 0
    #     while i < N - 1:
    #         while i < N - 1 and prices[i] >= prices[i + 1]:  # 取到=
    #             i += 1
    #         lo = i
    #         while i < N - 1 and prices[i] <= prices[i + 1]:  # 取到=
    #             i += 1
    #         hi = i  # [lo, hi]
    #         if prices[hi] > prices[lo]:  # 上面也可能因为N-1截止
    #             while stack and prices[lo] < prices[stack[-1][0]]: # 没有=
    #                 pl, ph = stack.pop() # 不参与做空
    #                 profits.append(prices[ph] - prices[pl])  # 做多的收益 
    #             while stack and prices[hi] >= prices[stack[-1][1]]:
    #                 pl, ph = stack.pop()
    #                 profits.append(prices[ph] - prices[lo]) # 做空的收益
    #                 lo = pl  # 修改范围
    #             stack.append((lo, hi))  # stack里都是还没计算profits的
    #             # profits.append(prices[hi] - prices[lo])  # 先不管做多的钱
    #     profits += [prices[hi] - prices[lo] for lo, hi in stack]
    #     return sum(heapq.nlargest(k, profits))

    def maxProfit(self, k, prices):
        N = len(prices)
        if N < 2:
            return 0
        if k >= N // 2:
            ans = 0
            for i in xrange(N - 1):
                ans += max(0, prices[i + 1] - prices[i])
            return ans
        # k + 1 还是能避免讨论
        f = [[0, float('-inf')] for _ in xrange(k + 1)]  # 初始化不能*k!!!
        for n in prices:
            for j in xrange(1, k + 1):
                f[j][0] = max(f[j][0], f[j][1] + n)
                f[j][1] = max(f[j][1], f[j - 1][0] - n)
        return f[-1][0]

if __name__ == '__main__':
    """
    总共k次操作.
    见123题
    """
    s = Solution()
    print(s.maxProfit(2, [2,4,1]))
    print(s.maxProfit(2, [3,2,6,5,0,3]))
# @lc code=end

