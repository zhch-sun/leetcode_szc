#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#

from itertools import combinations

# class Solution:
#     def combinationSum3(self, k, n):
#         return [c for c in combinations(range(1, 10), k) if sum(c) == n]

class Solution(object):
    # def combinationSum3(self, k, n):
    #     """
    #     :type k: int
    #     :type n: int
    #     :rtype: List[List[int]]
    #     """
    #     candi = list(range(1, 10))    
    #     res = []
    #     tmp = []
    #     self.backtrack(candi, n, tmp, 0, res, k)
    #     return res
    
    # def backtrack(self, candi, target, tmp, lo, res, k):
    #     if len(tmp) <= k:
    #         if target == 0 and len(tmp) == k:
    #             res.append(tmp[:])
    #         elif target > 0:
    #             for i in range(lo, len(candi)):  # 
    #                 tmp.append(candi[i])
    #                 self.backtrack(candi, target-candi[i], tmp, i + 1, res, k)
    #                 tmp.pop()

    def combinationSum3(self, k, n):
        # if n > (9 + 10 - k) * k // 2:
        #     return []
        target = n
        f = [[[] for __ in xrange(n + 1)] for _ in xrange(k + 1)]
        f[0][0] = [[]]
        for n in xrange(1, 10):
            # 结束条件是0, 因为内环中的i-1
            for i in xrange(k, 0, -1):  # Note 这也是反过来的...
                for j in xrange(target, n - 1, -1):
                    f[i][j] += [tmp + [n] for tmp in f[i - 1][j - n]]
        return f[-1][-1]
        
if __name__ == '__main__':
    """
    题设: 
        TODO: dfs貌似可以继续优化. 
        找出所有相加之和为n的k个数的组合。组合中只允许含有1-9的正整数，
        并且每种组合中不存在重复的数字。
        理解题意: 不是用1~k的数字, 而是1-9内的k个数. 
        39, 40 216 377
        TODO 和lintcode k-sum的区别是什么?? 貌似没有区别.. 
        k-sum经典的DP做法(复杂度?), 需要掌握. 和4-sum区别? 除重? 
    解法1:
        candi可以直接生成. 不需要sort. 
    TODO 代码参照40题的discuss应该可以修改? 
    TODO 复杂度分析? 包括所有backtrack的复杂度分析? 
    https://stackoverflow.com/questions/20049829/how-to-calculate-time-complexity-of-backtracking-algorithm
    循环时还有一个upper bound, 还有一个memo?
    https://leetcode.com/problems/combination-sum-iii/discuss/60621/My-C%2B%2B-solution-backtracking.
    
    解法2:
        这是个二维cost的背包, cost1: k个数, cost2: 和为target. value, 方案数
    """
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
