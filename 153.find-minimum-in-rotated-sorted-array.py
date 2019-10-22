#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#
import bisect

class Solution(object):
    def findMin(self, nums):
        if not nums:
            return
        lo, hi = 0, len(nums) - 1
        pivot = nums[-1]
        while lo < hi:  # 循环不变量只能 [lo, hi], 结束时lo==hi
            mid = lo + (hi - lo) // 2
            if nums[mid] > pivot:  # 也可以是nums[mid] >= nums[lo]
                lo = mid + 1  
            else:
                hi = mid  # -1 违背不变量
        return nums[lo]

    def findMax(self, nums):
        if not nums:
            return
        lo, hi = 0, len(nums) - 1
        pivot = nums[0]  # another pivot
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2  # ceiling division
            if nums[mid] < pivot:
                hi = mid - 1
            else: 
                lo = mid
        return nums[lo]


if __name__ == '__main__':
    """
    题设: 旋转一个数组, 找其中的最小值
    分析:
        对于插入位置型二分, 循环不变量是[lo, hi+1], 
        对于查找位置型二分, 循环不变量是[lo, hi]
    解法:
        查找最小值的pivot必须用nums[-1], 因为需要处理只有后半段的情况. 
        findMax: Ceiling division以及pivot位置变化
    """
    s = Solution()
    print(s.findMin([3,4,5,1,2]))
    print(s.findMin([3,1,2]))
    print(s.findMin([1]))
    print(s.findMin([1,2]))
    print(s.findMin([]))

    print(s.findMax([3,4,5,1,2]))
    print(s.findMax([3,1,2]))
    print(s.findMax([3,4,1,2]))
    print(s.findMax([1]))
    print(s.findMax([1,2]))
    print(s.findMax([1,2,3,4]))
