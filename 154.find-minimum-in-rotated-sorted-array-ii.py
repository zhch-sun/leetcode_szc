#
# @lc app=leetcode id=154 lang=python
#
# [154] Find Minimum in Rotated Sorted Array II
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 88%
        left, right = 0, len(nums) - 1
        while left < right and nums[left] == nums[right]:  # Note 判断条件
            left += 1
        # loop invariant [left, right]
        # exit left == right
        # always move
        while left < right:
            # if nums[left] < nums[right]:
            #     return nums[left]
            mid = (right - left) // 2 + left
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == '__main__':
    """
    所有做法最坏情况的复杂读都是O(n)
    """
    s = Solution()
    print(s.findMin([1,3,5]))
    print(s.findMin([2,2,2,0,1]))
    print(s.findMin([1,1,1,2,0,1,1,1,1]))
    print(s.findMin([1,1]))
