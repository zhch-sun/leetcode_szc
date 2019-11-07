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
    #     # 900ms 87%
    #     f = [float('inf')] * (amount + 1)
    #     f[0] = 0  # Note 这里是0...
    #     for c in coins:
    #         for j in xrange(c, amount + 1):
    #             f[j] = min(f[j], f[j - c] + 1)  # Note 漏了+1...
    #     return -1 if f[-1] == float('inf') else f[-1]
    
    def coinChange(self, coins, amount):
        # 48ms vs 其他人最好 56ms
        def dfs(idx, target, cnt):
            if idx == len(coins):
                return
            if (target + coins[idx] - 1) // coins[idx] + cnt >= self.ans:
                return
            if target % coins[idx] == 0:
                self.ans = min(self.ans, cnt + target // coins[idx])
                return 
            for j in xrange(target // coins[idx], -1, -1):  # 可能取0个
                dfs(idx + 1, target - coins[idx] * j, cnt + j)

        self.ans = float('inf')
        coins = list(set(coins))  # 确实可以加速...
        coins.sort(reverse=True)
        dfs(0, amount, 0)
        return -1 if self.ans == float('inf') else self.ans

if __name__ == '__main__':
    """
    题设: 用最小个数的硬币构成钱数. 
        518题换硬币2, 不考虑硬币顺序, 377题考虑顺序. 
    分析: 
        值二分应该是不行, 无法greedy确定最优解. 
        容易看出是完全背包. 
        类似416题, 也可以DFS. 而且速度更快. 
        之所以可以优化, 是因为cost和value是相关的? 币值越大可能的value就越小.
    解法1: O(amount * len(coins))
        完全背包, 递推公式推导. 
        状态: 只用前i个硬币构成j钱的最小个数. 
        f[i][j] = min(f[i-1][j], f[i-1][j-c]+1, f[i-1][j-2c]+1, f[i-1][j-kc]+1)
        f[i][j-c] =          min(f[i-1][j-c]+1, f[i-1][j-2c]+1, f[i-1][j-kc]+1)
        f[i][j] = min(f[i-1][j], f[i-1][j-c]+1)
    解法2: O(amount * len(coins)) 不需要dp数组!
        从大到小dfs + 剪枝 快十倍. 
        加速方法: 
            1. 可以通过target % coins[idx], 即除法来代替若干个加法. 
            2. 剪枝: 利用当前硬币的理论最小个数和当前ans相比较. 
        但是的dfs是可以的. 需要给一个正确的bound. 
    """
    s = Solution()
    print(s.coinChange([1,2,5], 11))
    print(s.coinChange([2], 3))
        