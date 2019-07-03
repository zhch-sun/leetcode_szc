#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#
class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     res = [0, nums[0]]
    #     for i in range(1, len(nums)):
    #         res.append(max(res[i], res[i-1]+nums[i]))
    #     return res[-1]

    def rob(self, nums):
        # fastest
        l, r = 0, 0
        for n in nums:
            l, r = r, max(n + l, r)
        return r

if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.rob([2,7,9,3,1]))

