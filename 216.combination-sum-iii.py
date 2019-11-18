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
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candi = list(range(1, 10))    
        res = []
        tmp = []
        self.backtrack(candi, n, tmp, 0, res, k)
        return res
    
    def backtrack(self, candi, target, tmp, lo, res, k):
        if len(tmp) <= k:
            if target == 0 and len(tmp) == k:
                res.append(tmp[:])
            elif target > 0:
                for i in range(lo, len(candi)):  # 
                    tmp.append(candi[i])
                    self.backtrack(candi, target-candi[i], tmp, i + 1, res, k)
                    tmp.pop()

    # def combinationSum3(self, k, n):
    #     # if n > (9 + 10 - k) * k // 2:
    #     #     return []
    #     target = n
    #     f = [[[] for __ in xrange(n + 1)] for _ in xrange(k + 1)]
    #     f[0][0] = [[]]
    #     for n in xrange(1, 10):
    #         # 先对个数循环, 结束条件是0, 因为内环中的i-1
    #         for i in xrange(k, 0, -1):  # Note 逆序
    #             for j in xrange(target, n - 1, -1):  # 再对target循环 
    #                 f[i][j] += [tmp + [n] for tmp in f[i - 1][j - n]]
    #     return f[-1][-1]
        
if __name__ == '__main__':
    """
    题设: 
        找出所有相加之和为n的k个数的组合。数字范围1-9. 没有重复啊. 
        并且每种组合中不存在重复的数字
        39, 40 216 377
        即lintcode的k-sum, 4-sum是多重背包, 这题01背包即可. 
    解法1:
        20ms 53%
        candi可以直接生成. 不需要sort. 
        TODO: dfs貌似可以继续优化.         
        TODO 代码参照40题的discuss应该可以修改? 
        TODO 复杂度分析? 包括所有backtrack的复杂度分析? 
        https://stackoverflow.com/questions/20049829/how-to-calculate-time-complexity-of-backtracking-algorithm
        循环时还有一个upper bound, 还有一个memo?
        https://leetcode.com/problems/combination-sum-iii/discuss/60621/My-C%2B%2B-solution-backtracking.
    
    解法2:
        20ms, 53%
        二维cost的背包, cost1: k个数, cost2: target. value是方案数
        f[idx][i][j] idx: item, i, 数字个数, j target
    """
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
