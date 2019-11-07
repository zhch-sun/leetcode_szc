#
# @lc app=leetcode id=518 lang=python
#
# [518] Coin Change 2
#

# @lc code=start
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins = list(set(coins))
        f = [0] * (amount + 1)
        f[0] = 1
        for c in coins:
            for j in xrange(c, amount + 1):  # 必须是c开头
                f[j] += f[j - c]
        return f[-1]
        
if __name__ == '__main__':
    """
    题设: 无穷的硬币个数有限的硬币种类, 计算组成target的组合数.
    分析:
        完全背包和01背包416题不完全一样, 不完全是素数筛法. 
        第c个硬币的时, 按间隔c用j-c更新f数组. 而不是只按照  
        没有二进制优化. 一方面存储的不是二进制, 另一方面即使是二进制也不能避免内环.
    分析: 完全背包问题, 就是要这样一步一步优化
    解法: 
        完全背包推导:
        f[i][j]=f[i-1][j] + f[i-1][j-c], ..., + f[i-1][j-tc]
        f[i][j-c]=          f[i-1][j-c], ..., + f[i-1][j-tc]
        f[i][j] = f[i-1][j] + f[i-1][j-c]
    解法:
        错解1:
            这是377题的解法, 相当于 permutation sum
            状态: 集合: 第j块钱的 硬币组合, 属性: 个数
            状态转移: f[i] = sigma(k, f[i - k])  会有重复!!!
        状态: 
            集合: 前i种硬币凑出j的凑法, 属性: 个数
            状态转移: 根据第i种硬币的个数! 分别讨论.  (复杂度 N3)
            滚动数组: 
                f[i][j]只和上一层和本一层有关, 可以滚动数组
                特殊: 依赖性是上一个和左一个的时候, 可以一维数组 (复杂度 N2)
    """
    s = Solution()
    print(s.change(5, [1,2,5]))
    print(s.change(3, [2]))
    print(s.change(10, [10]))
# @lc code=end

