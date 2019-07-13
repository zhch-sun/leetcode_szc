#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        left = 0
        candidates.sort()
        self.backtrack(candidates, target, res, left, tmp)
        return res

    def backtrack(self, candidates, target, res, left, tmp):
        if target == 0:
            res.append(tmp[:])
        elif target > 0:
            for i in range(left, len(candidates)):
                # 仍然需要过滤1123这种. 注意是i-left不是i!!!
                if i - left > 0 and candidates[i] == candidates[i-1]:
                    continue
                tmp.append(candidates[i])
                self.backtrack(candidates, target-candidates[i], res, i+1, tmp)
                tmp.pop()

if __name__ == '__main__':
    """
    注意过滤条件. 
    """
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))
