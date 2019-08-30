#
# @lc app=leetcode id=852 lang=python
#
# [852] Peak Index in a Mountain Array
#
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo, hi = 0, len(A) - 1
        while lo < hi:  # invariant [lo, hi]
            mid = lo + (hi - lo) // 2
            if A[mid] < A[mid+1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
        
if __name__ == '__main__':
    """
    len(nums) > 3, 相邻元素不等.
    """
    s = Solution()
    print(s.peakIndexInMountainArray([0,2,1,0]))
    print(s.peakIndexInMountainArray([0,1,0]))
