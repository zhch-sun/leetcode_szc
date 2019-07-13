#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        self.backtrack(nums, res, tmp, 0)
        return res

    def backtrack(self, nums, res, tmp, pos):
        res.append(tmp[:])
        for i in range(pos, len(nums)):
            tmp.append(nums[i])
            self.backtrack(nums, res, tmp, i + 1)
            tmp.pop()


if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.subsets([1,2,3]))

