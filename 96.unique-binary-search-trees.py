#
# @lc app=leetcode id=96 lang=python
#
# [96] Unique Binary Search Trees
#
class Solution(object):
    # def numTrees(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 0:
    #         return 0  # why don't need that?
    #     dp = [0] * (n + 1)  # n+1 here
    #     dp[1] = dp[0] = 1  # shouldn't init with 0!
    #     for i in range(2, n + 1):
    #         for j in range(1, i + 1):
    #             dp[i] += dp[i - j] * dp[j - 1]  # note this is j - 1
    #     return dp[-1]

    def numTrees(self, n):
        # half loop optimization
        dp = [0] * (n + 1)  # n+1 here
        dp[1] = dp[0] = 1  # shouldn't init with 0!
        for i in range(2, n + 1):
            for j in range(1, int(i/2) + 1):
                dp[i] += 2 * dp[i-j] * dp[j-1]
            if i % 2 == 1:  # i is current n !!
                # Accoding to formula, it's not i/2+1 ! though the center is.
                dp[i] += dp[i/2] * dp[i/2]  
        return dp[n]
        
if __name__ == '__main__':
    """
    关键在于以某个数为中心的个数等于左右两遍的个数的乘积. 
    """
    s = Solution()
    print(s.numTrees(5))
