#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#
class Solution(object):
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     dp = [0] * (n + 1)
    #     dp[1] = dp[0] = 1  # Note dp[0] is strange
    #     #  dp[2] = 2  # Note the input might be 1!!!
    #     for i in range(2, n + 1):
    #         dp[i] = dp[i-1] + dp[i-2]  # fibonacci
    #     return dp[n]

    def climbStairs(self, n):
        # f[i] = f[i - 1] + f[i - 2]
        if n <= 2:
            return n
        pre, cur = 1, 2
        for _ in xrange(3, n + 1):  # n + 1
            pre, cur = cur, pre + cur
        return cur

if __name__ == '__main__':
    """
    状态转移公式: 
        f[i] = f[i - 1] + f[i - 2]
    斐波那契数列
    """
    s = Solution()
    print(s.climbStairs(3))
    print(s.climbStairs(4))
        

