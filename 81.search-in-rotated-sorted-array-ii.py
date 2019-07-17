#
# @lc app=leetcode id=81 lang=python
#
# [81] Search in Rotated Sorted Array II
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 90%
        left = 0
        right = len(nums) - 1
        while right > 0 and nums[left] == nums[right]:
            right -= 1
        while left <= right:
            mid = (right - left) // 2 + left
            # 问题处在下面这个条件判断上, 比如1311111
            # mid其实在右边, 但是mid = nums[0] 且 target > nums[0]
            # 这样意味mid和target都在左边. 
            # 所以只要确保nums[0]唯一就可以了. 
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif target < nums[0]:
                left = mid + 1
            elif target > nums[0]:
                right = mid - 1
            else:
                return True
        return False

if __name__ == '__main__':
    """
    """
    s = Solution()
    # print(s.search([2,5,6,0,0,1,2], 2))
    print(s.search([1,3,1,1,1,1,1], 3))
    # print(s.search([], 3))
