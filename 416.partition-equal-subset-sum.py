#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = sum(nums)  # note use target instead of sums
        if target % 2 == 1:
            return False
        target /= 2
        dp = [True] + [False] * target
        for num in nums:
            for t in range(target, num - 1, -1):
                if t >= num:
                    dp[t] = dp[t] or dp[t - num]
        return dp[target]

        
if __name__ == '__main__':
    """
    这个转换为有没有 一个组合的和是 sum/2. 这和coin change 非常相似. 区别只在于每个数只能用一次.
    这个区别导致内环需要递减, 而coin change内环递增. 
    因为当递增的时候, 在内环dp[15]=False, dp[5]=5, num=5的时候, dp[5]和dp[10]都会被Ture! 但实际只能有一个.
    TODO 通过0-1背包问题再写一个答案?
    TODO DFS更快...
    """
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))
    print(s.canPartition([1, 2, 3, 5]))
