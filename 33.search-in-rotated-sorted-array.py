#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) / 2 + left
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            elif target < nums[0]:  # 不在同一个半区的时候肯定值不一样. 
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == '__main__':
    """
    必须有在最上面判断符为<=的时候 必须有+1和-1, 
    还是这种最好理解..
    """
    s = Solution()
    # print(s.search([4,5,6,7,0,1,2], 4))
    # print(s.search([4,5,6,7,0,1,2], 5))
    # print(s.search([4,5,6,7,0,1,2], 2))
    print(s.search([1,3], 2))
