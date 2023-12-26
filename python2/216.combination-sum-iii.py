#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#

from itertools import combinations

class Solution(object):
    # def combinationSum3(self, k, n):
    #     return [c for c in combinations(range(1, 10), k) if sum(c) == n]
    
    def combinationSum3(self, k, target):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """           
        def dfs(tmp, idx, target):
            if len(tmp) == k and target == 0:
                ans.append(tmp[:])
                return
            for j in xrange(idx, 10 - (k - len(tmp)) + 1):  # 剪枝1
                if target >= j:
                    tmp.append(j)
                    dfs(tmp, j + 1, target - j)
                    tmp.pop()
                else:
                    break  # 剪枝2
            return
        ans = []
        dfs([], 1, target)
        return ans

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
        找出所有相加之和为n的k个数的组合。可用数字范围1-9. 
        c(9, k) 并且每种组合中不存在重复的数字
        39, 40 216 377
        这道题是lintcode的k-sum, 4-sum是多重背包, 这题01背包即可. 
    解法1:
        回溯, 确保升序从而除重. 因为k个数可以剪枝
        复杂度: c(9, k) * k. k是复制array的时间.
        https://stackoverflow.com/questions/20049829/how-to-calculate-time-complexity-of-backtracking-algorithm
    解法2:
        剪枝未写: 循环时还有一个upper bound, 还有一个memo?
        https://leetcode.com/problems/combination-sum-iii/discuss/60621/My-C%2B%2B-solution-backtracking.
    解法3:
        二维cost的背包, cost1: k个数, cost2: target. value是方案数
        f[idx][i][j] idx: item, i, 数字个数, j target
    """
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))
    print(s.combinationSum3(3, 15))
