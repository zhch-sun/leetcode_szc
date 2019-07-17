#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: # at least two nums
            return 0 
        left, right = 0, len(nums) - 1
        # loop invariant [left, right] 存在性. 
        while left < right:  # 跳出的时候 left=right
            mid = (right - left) // 2 + left
            if nums[mid] < nums[mid+1]: # 右边一定有解.
                left = mid + 1
            else:
                right = mid  # 因为//会自动左移一位, 所以收敛性可以保证. 
        return left


if __name__ == '__main__':
    """
    TODO 这个也是852题. 
    答案实际上在求中间位置的梯度.
    需要用循环不变量来解释, 如下链接
    https://leetcode.com/problems/find-peak-element/discuss/50239/Java-solution-and-explanation-using-invariants
    """
    s = Solution()
    # print(s.findPeakElement([1,2,3,1,2,3]))
    # print(s.findPeakElement([1,2,3,1]))
    # print(s.findPeakElement([1,2,1,3,5,6,4]))
    print(s.findPeakElement([1]))
