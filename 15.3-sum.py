#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def sortedTwoSum(self, nums, left, target):
        l = left
        r = len(nums) -1
        res = []
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
                res.append([target * -1, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:  # Note this sign!
                    l += 1
                while l < r and nums[r] == nums[r + 1]:  # Note sign!
                    r -= 1                
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 97 %
        nums.sort()
        res = []
        for idx, item in enumerate(nums):
            if nums[idx] > 0:  # pruning
                break
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            target = -1 * item
            res += self.sortedTwoSum(nums, idx + 1, target)
        return res


if __name__ == '__main__':
    """
    注意有 -1, -1, 2这种搭配, 所以不能在最前面搞一个set!!!!
    思路1 sort之后每个元素来, 剩下的两个元素就是一个sorted 2sum. 
         问题是duplicates, 一个是2sum内的重复, 一个是2sum间的重复
    """
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

