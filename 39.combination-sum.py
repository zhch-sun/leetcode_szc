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
        def dfs(candidates, target, res, tmp, left):
            # 把dfs放进来提速效果显著..
            if target == 0:
                res.append(tmp[:])
            elif target > 0:
                for i in range(left, len(candidates)):
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
    和N-sum的区别在于，这个不限制N的个数。因此也只能用dfs穷举
    backtracking: 算sum不如target-item快.
    TODO: 还有dp的做法? 应该就不记了. 
    """
    s = Solution()
    print(s.combinationSum([2,3,5], 8))
