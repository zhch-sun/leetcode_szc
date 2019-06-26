#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # this is 98%
        sums = sum(nums)
        target = S + sums
        if target % 2 == 1 or sums < S:
            return 0
        target /= 2

        # Note that leads to memory error...has to check before
        dp = [1] + [0] * target  
        for num in nums:
            for i in xrange(target, num - 1, -1):  # Note the xrange
                if dp[i - num]:
                    dp[i] += dp[i - num]   # Note not + 1!
        
        return dp[target]

if __name__ == '__main__':
    """
    必须是正数?
    TODO DFS
    """
    s = Solution()
    print(s.findTargetSumWays([1,2,7,9,981], 1000000000000))
        

