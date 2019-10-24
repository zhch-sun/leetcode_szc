#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # note this fastest initial method! not list comprehension

        for i in range(1, n):
            for j in range(0, i):
                # 第一种实现 (哪种更好呢?)
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                # 另一种实现 
                # if nums[i] > nums[j]:
                #     dp[i] = max(dp[j] + 1, dp[i])
        
        maximum = max(dp)  # max can not take [] input!!!
        return maximum

if __name__ == '__main__':
    """
    dynamic programming
    还有一个patience sorting, 可以二分, 但是需要很多证明..
    https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
    """
    s = Solution()
    array = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(array))

