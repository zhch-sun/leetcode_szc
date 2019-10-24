#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, res, tmp, lo):
            # 把dfs放进来提速效果显著..
            if target == 0:
                res.append(tmp[:])
            elif target > 0:
                # 因为需要重用同一个字符, 所以lo不加1
                for i in range(lo, len(candidates)):
                    item = candidates[i]
                    if item > target:  # 加速效果显著
                        break
                    tmp.append(item)
                    dfs(candidates, target-item, res, tmp, i)
                    tmp.pop()
        res = []
        tmp = []
        candidates.sort()
        dfs(candidates, target, res, tmp, 0)
        return res

if __name__ == '__main__':
    """
    题设: 
        给定一个无重复元素的数组和一个目标数，
        找出数组中所有可以使数字和为target的组合。 数组中数可以无限选取.
        39 40 216
    解法: 
        和N-sum的区别在于，这个不限制N的个数。因此也只能用dfs穷举
        backtracking: 算sum不如target-item快.
    复杂度:
        因为无限选数复杂度不太好分析.. 先不管了. 
    TODO: 还有dp的做法? 应该就不记了. 
    """
    s = Solution()
    print(s.combinationSum([2,3,5], 8))
