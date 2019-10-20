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
        nums.sort()
        closest = float('inf')
        for idx, item in enumerate(nums):
            l = idx + 1
            r = len(nums) - 1
            while l < r:
                cur = item + nums[l] + nums[r] 
                closest = closest if abs(target-closest) < abs(target-cur) \
                    else cur
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    return target
        return closest
        
if __name__ == '__main__':
    """
    应该判断len(nums)>3
    TODO pruning法？3*item-target>abs(target-closest)
    """
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], -1))

