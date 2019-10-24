#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#
class Solution(object):
    def findPeakElement(self, nums):
        if not nums:  # 只有一个元素时直接返回0
            return
        lo, hi = 0, len(nums) - 1
        while lo < hi:  # 不变量 [lo, hi]
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1  # mid + 1时可能的解 [lo
            else:
                hi = mid   # mid是可能的解 hi]
        return lo

if __name__ == '__main__':
    """
    题设: 
        峰值元素是大于左右两边的元素. 找到任意一个即可.
        相邻元素不相等. nums[-1] = nums[n] = -∞
        852题更简单, 整个array是一个mountain, 找最大值.
    解法:
        可以证明一定有解;
        求中间位置梯度之后, 梯度增长方向一定有解:
            1. 一直增长, 则解在最右边
            2. 先增再降, 则解是那个高点.
        注意相邻位置不会相等. 重要条件.
    """
    s = Solution()
    # print(s.findPeakElement([1,2,3,1,2,3]))
    print(s.findPeakElement([1,2,3,1]))
    print(s.findPeakElement([1,2,1,3,5,6,4]))
    print(s.findPeakElement([1]))
