#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#
class Solution(object):
    # def coinChange(self, coins, amount):
    #     """
    #     :type coins: List[int]
    #     :type amount: int
    #     :rtype: int
    #     """
    #     # 64%
    #     maximum = amount + 1
    #     dp = [maximum for _ in range(amount + 1)]
    #     dp[0] = 0
    #     for cur in range(1, amount + 1):
    #         for coin in coins:
    #             if coin <= cur:
    #                 dp[cur] = min(dp[cur], dp[cur - coin] + 1) 
    #     # print(dp, amount, dp[amount])
    #     return dp[amount] if dp[amount] < maximum else -1
    
    def coinChange(self, coins, amount):
        # 76%
        maximum = amount + 1
        dp = [maximum for _ in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for cur in range(coin, amount + 1):
                dp[cur] = min(dp[cur], dp[cur - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1

if __name__ == '__main__':
    """
    一个简单的dp就是for循环i.
    另一个改进是外层for循环coin, 这样 < coin的i就不需要了. 总共可以节省sum(coins)的计算, 
    而且这样不需要sort coins, 可以认为第一遍是用coins[0]的最优情况, 第二遍是用coins[0:2]的最优
    TODO: binary search是最优解...
    """
    s = Solution()
    print(s.coinChange([1,2,5], 11))
    print(s.coinChange([2], 3))
        

