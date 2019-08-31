#
# @lc app=leetcode id=719 lang=python
#
# [719] Find K-th Smallest Pair Distance
#
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def count(nums, mid, N):
            i, j = 0, 1  # 0,0 亦可
            cnt = 0
            while i < N:
                while j < N and nums[j] - nums[i] <= mid:
                    j += 1  # j = 1的时候没有元素..
                cnt += j - i - 1  #精彩.
                i += 1
            return cnt
            
        N = len(nums)
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:  # [lo, hi]
            mid = lo + (hi - lo) // 2
            cnt = count(nums, mid, N)
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
if __name__ == '__main__':
    """
    精彩的双指针. 
    """
    s = Solution()
    print(s.smallestDistancePair([1,3,1], 1))

