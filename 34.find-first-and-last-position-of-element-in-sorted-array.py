#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search_left(nums, target, left, right):
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def search_right(nums, target, left, right):
            while left <= right:
                mid = (right - left) // 2 + left
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        # this is 86
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                left = search_left(nums, target, left, mid)
                right = search_right(nums, target, mid, right)
                return [left, right-1]  # Note this -1!!!!
        return [-1, -1]
        # This is 96
        # left = search_left(nums, target, 0, len(nums) - 1)
        # right = search_right(nums, target, left, len(nums) - 1) - 1
        # return [left, right] if left <= right else [-1, -1]

if __name__ == '__main__':
    """
    见35题
    居然只有84%. 
    简单的search left 和 right居然更快....
    """
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 7))

