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
        if n <= 2:
            return n
        item0, item1 = 1, 1
        for _ in range(2, n + 1):
            # the logic below is faster than swap item1 item0
            tmp = item1
            item1 = item0 + item1
            item0 = tmp
        return item1

if __name__ == '__main__':
    """
    Note also can use const space
    """
    s = Solution()
    print(s.climbStairs(3))
        

