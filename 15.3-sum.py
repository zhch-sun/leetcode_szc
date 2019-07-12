#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def sortedTwoSum(self, nums, left, target, res):
        l = left
        r = len(nums) -1
        while l < r:
            cur = nums[l] + nums[r]
            if cur < target:
                l += 1
                # while l < r and nums[l] == nums[l - 1]:  # Not fast
                #     l += 1          
            elif cur > target:
                r -= 1
                # while l < r and nums[r] == nums[r + 1]:  # not fast
                #     r -= 1                
            else:
                res.append([0 - target, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:  # Note this sign!
                    l += 1
                while l < r and nums[r] == nums[r + 1]:  # Note sign!
                    r -= 1                

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 98 %
        nums.sort()
        res = []
        for idx in xrange(len(nums)-1):
            item = nums[idx]
            if nums[idx] > 0:  # pruning: 这是res里面的最小值. 
                break
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            self.sortedTwoSum(nums, idx + 1, 0 - item, res)
        return res


if __name__ == '__main__':
    """
    注意有 -1, -1, 2这种搭配, 所以不能在最前面搞一个set!!!!
    思路1 sort之后每个元素来, 剩下的两个元素就是一个sorted 2sum. 
         问题是duplicates, 一个是2sum内的重复, 一个是2sum间的重复
    """
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

