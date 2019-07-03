#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#
class Solution(object):


    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def twoSum(nums, target, left, closest):
            l = left
            r = len(nums) - 1
            while l < r:
                cur = nums[l] + nums[r]
                closest = closest if abs(closest) < abs(target - cur) else target - cur
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    return target

        nums.sort()
        closest = float('inf')
        for idx, item in enumerate(nums):
            closest = twoSum(nums, target - item, idx + 1, closest) + item
            if closest == target:
                return closest
        return closest
        
if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], -1))

