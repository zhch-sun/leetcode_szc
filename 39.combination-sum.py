#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
class Solution(object):
    # def combinationSum(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     def dfs(candidates, target, res, tmp, lo):
    #         # 把dfs放进来提速效果显著..
    #         if target == 0:
    #             res.append(tmp[:])
    #         elif target > 0:
    #             # 因为需要重用同一个字符, 所以lo不加1
    #             for i in xrange(lo, len(candidates)):
    #                 item = candidates[i]
    #                 if item > target:  # 加速效果显著
    #                     break
    #                 tmp.append(item)
    #                 dfs(candidates, target-item, res, tmp, i)
    #                 tmp.pop()
    #     res = []
    #     tmp = []
    #     candidates.sort()
    #     dfs(candidates, target, res, tmp, 0)
    #     return res

    def combinationSum(self, candidates, target):
        f = [[] for _ in xrange(target + 1)]
        f[0] = [[]]  # Note: 震惊! 初始化! 理解这个初始化含义!
        for n in candidates:
            for j in xrange(n, target + 1):
                f[j] += [tmp + [n] for tmp in f[j-n]]
        return f[-1]

if __name__ == '__main__':
    """
    题设: 
        给定一个无重复元素的数组和一个目标数，均为正整数. 
        无限选数, 返回使数字和为target的所有组合. list of list
        同类题目: 39 40 216 377
    解法: 
        dfs + backtrack. 
        和N-sum的区别在于，这个不限制N的个数。因此也只能用dfs穷举
        backtracking: 算sum不如target-item快.
        可以继续pruning, 不管了.
        复杂度:
            TODO 无限选数复杂度不太好分析? 见下面链接.  
            https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
    解法2: DP, 
        完全背包, 但是返回的是具体的方案! 需要修改状态的定义. 
        空间复杂度比dfs还是变大很多. 
    """
    s = Solution()
    print(s.combinationSum([2,3,5], 8))
    print(s.combinationSum([2,3,6,7], 7))
