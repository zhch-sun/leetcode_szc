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
        res = []
        tmp = []
        left = 0
        candidates.sort()
        self.backtrack(candidates, target, res, tmp, left)
        return res

    def backtrack(self, candidates, target, res, tmp, left):
        if target == 0:
            res.append(tmp[:])
        elif target > 0:
            for i in range(left, len(candidates)):
                item = candidates[i]
                tmp.append(item)
                self.backtrack(candidates, target-item, res, tmp, i)
                tmp.pop()

if __name__ == '__main__':
    """
    backtracking: 算sum不如target-item快.
    """
    s = Solution()
    print(s.combinationSum([2,3,5], 8))
