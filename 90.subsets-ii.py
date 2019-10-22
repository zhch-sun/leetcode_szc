#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        nums.sort()  # 别忘了sort..
        self.backtrack(nums, res, tmp, 0)
        return res

    def backtrack(self, nums, res, tmp, pos):
        res.append(tmp[:])
        for i in xrange(pos, len(nums)):
            if i > pos and nums[i] == nums[i-1]:
                continue
            tmp.append(nums[i])
            self.backtrack(nums, res, tmp, i + 1)
            tmp.pop()

if __name__ == '__main__':
    """
    题设: 78题第一个, 区别是允许重复
    思路: 在同一个循环中如果遇到重复则continue, TODO 证明?
    TODO iterative solution
    """
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))
