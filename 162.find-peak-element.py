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
    答案实际上在求中间位置的梯度, 梯度增长的方向一定有解; 注意相邻位置不会相等. 重要条件.
    852题更简单, 整个array mountain, 找最大值.
    """
    s = Solution()
    # print(s.findPeakElement([1,2,3,1,2,3]))
    print(s.findPeakElement([1,2,3,1]))
    print(s.findPeakElement([1,2,1,3,5,6,4]))
    print(s.findPeakElement([1]))
