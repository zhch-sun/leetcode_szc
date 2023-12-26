#
# @lc app=leetcode id=123 lang=python
#
# [123] Best Time to Buy and Sell Stock III
#
import heapq
class Solution(object):
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     N = len(prices)  # 处理特殊值.
    #     stack = []
    #     profits = []
    #     i = 0
    #     while i < N - 1:
    #         # 也有用两个变量v和p存储的, 似乎还是用i心智复杂度最低.
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
    #                 # 这里不能push做空区间进stack, 也不能pop上一个profits
    #                 profits.append(prices[ph] - prices[lo]) # 做空的收益
    #                 lo = pl  # 修改范围
    #             stack.append((lo, hi))  # stack里都是还没计算profits的
    #             # profits.append(prices[hi] - prices[lo])  # 先不管做多的钱
    #     profits += [prices[hi] - prices[lo] for lo, hi in stack]
    #     return sum(heapq.nlargest(2, profits))

    # def maxProfit(self, prices):
    #     N = len(prices)
    #     if N < 2:
    #         return 0
    #     k = 2
    #     # 不考虑初始化, 其实总共就是四个状态. 所以可以优化成状态机, k+1才是正确初始化
    #     f = [[0, float('-inf')] for _ in xrange(k + 1)]# 初始化不能*k!!!
    #     for n in prices:
    #         for j in xrange(1, k + 1):
    #             f[j][0] = max(f[j][0], f[j][1] + n)
    #             f[j][1] = max(f[j][1], f[j - 1][0] - n)
    #     return f[-1][0]

    def maxProfit(self, prices):
        s1, s2 = 0, 0  # hold and sold
        h1, h2 = float('-inf'), float('-inf')
        for n in prices:
            s1 = max(s1, h1 + n)
            h1 = max(h1, - n)  # 需要在h1下面, 而且是0-n
            s2 = max(s2, h2 + n)
            h2 = max(h2, s1 - n)
        return max(s1, s2)

if __name__ == '__main__':
    """
    题设: 最多完成两笔交易.
    解法1:
        看成若干峰peak谷valley. 只有谷-峰是可以赚钱的.
        现在找到所有v-p对, 因为不能同时交易, 所以考虑连续的vp对
        有些pair合并之后比两个都大, 则合并, 此时:
            关键: 同时添加一次做空操作和相应收益! 
        这样, 我们列出了所有能赚钱的操作: 做多+做空
            操作个数(做多+多空)和vp对的个数一致,
            且已经greedy的合并了所有可以合并的操作
        坑: 
            需要分类讨论各种vp pair的组合情况. 
            合并条件是 v1 <= v2 and p1 <= p2, 可以推导出来.
            然而v1 p1 v2 p2的各种大小比较都需要照顾到.
                三种情况:
                    未来一定不能合并(第一个while): 因为lo比后面更高, 合起来不行 
                    正在合并(第二个while), 
                    未来可能合并(留在栈内)
                图示: case3 http://www.tachenov.name/2016/02/14/128/
            结果是stack内存储v2 > v1, p2 < p1的上升沿
            并不"单调". 可以跨过若干stack内元素, 再一起合并. 
    解法2:
        DP思路, 难点在于多了一个持有的状态位
        DP其实就是一个记录前I个状态历史的状态机!!!
        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen/
        f[i][k][s]. 已经最多k笔(未卖出也算1笔), 第i天, 当天是否持有股票s
        状态转移: 有买卖空三种操作
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        初始化: 
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
        状态转移优化: i 只依赖于 i - 1, 去掉i这一位.
            dp[k][0] = max(dp[k][0], dp[k][1] + prices[i])
            dp[k][1] = max(dp[k][1], dp[k-1][0] - prices[i])  # 注意负号!
        初始化: 
            dp[0][0] = 0
            dp[0][1] = float('-inf')
    解法3:
        考虑只有两次操作, 那么状态实际就四种, 四个max是最快的解法.
        h1 s1 h2 s2表示四种持有或者已经卖出的状态
            s1 = max(s1, h1 + n)
            h1 = max(h1, - n)
            s2 = max(s2, h2 + n)
            h2 = max(h2, s1 - n)

    """
    s = Solution()
    print(s.maxProfit([2,4,1]))
    print(s.maxProfit([3,2,6,5,0,3]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))
    print(s.maxProfit([3,3,5,0,0,3,1,4]))  # 6
    print(s.maxProfit([2,1,2,0,1]))  # 2


