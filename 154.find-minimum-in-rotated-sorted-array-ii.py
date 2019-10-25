#
# @lc app=leetcode id=154 lang=python
#
# [154] Find Minimum in Rotated Sorted Array II
#
class Solution(object):
    def findMin(self, nums):  # 99%
        # 不变量[lo, hi]
        if not nums:
            return
        lo, hi = 0, len(nums) - 1
        pivot = nums[-1]
        while lo < hi and nums[lo] == pivot:
            lo += 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > pivot:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

if __name__ == '__main__':
    """
    存在重复. 除重时需要留一个元素. 
    所有做法最坏情况的复杂度都是O(n)
    """
    s = Solution()
    print(s.findMin([1,3,5]))
    print(s.findMin([2,2,2,0,1]))
    print(s.findMin([1,1,1,2,0,1,1,1,1]))
    print(s.findMin([1,1]))
    print(s.findMin([1,2]))
