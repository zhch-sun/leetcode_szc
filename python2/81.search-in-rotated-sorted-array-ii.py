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
        if not nums:
            return False
        lo, hi = 0, len(nums) - 1
        pivot = nums[0]  # 仍然用nums[0]当pivot
        while hi > 0 and pivot == nums[hi]:  # 不能>=0, 需要留一个数
            hi -= 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if (nums[mid] < pivot)  == (target < pivot):
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return True
            elif nums[mid] < target:
                hi = mid - 1
            else:  # 不可能相等.
                lo = mid + 1
        return False

if __name__ == '__main__':
    """
    题设: 33题是第一题. 区别是允许重复
    解法:
        只要保证pivot只出现在左边即可. 注意左边仍然有可能有多个pivot. 
        条件判断时可以两个小于号, 也可以两个>=号
    """
    s = Solution()
    print(s.search([2,5,6,0,0,1,2], 2))
    print(s.search([1,3,1,1,1,1,1], 3))
    print(s.search([], 3))
