#
# @lc app=leetcode id=312 lang=python
#
# [312] Burst Balloons
#

# @lc code=start
class Solution(object):
    # def maxCoins(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     def dfs(i, j):  # [i, j]
    #         if i > j: 
    #             return 0
    #         if (i, j) in f:  # 必须加括号的原因是in和逗号的优先级..
    #             return f[i, j]
    #         ans = float('-inf')
    #         for k in xrange(i, j + 1):
    #             cur = nums[k] * nums[i - 1] * nums[j + 1] + \
    #                 dfs(i, k-1) + dfs(k+1, j)
    #             ans = max(ans, cur)
    #         f[i, j] = ans  # 特别容易忘..
    #         return ans
            
    #     if not nums:
    #         return 0  # 这时return 0...
    #     nums = [1] + nums + [1]  # 大家还是都加了sentinel
    #     N = len(nums)  # Note 加哨兵之后再求N
    #     f = {}
    #     return dfs(1, N - 2)

    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        N = len(nums)
        f = [[0] * N for _ in xrange(N)]
        for j in xrange(1, N - 1):
            for i in xrange(j, 0, -1):  # 0取不到
                ans = float('-inf')
                for k in xrange(j, i - 1, -1):
                    cur = nums[k] * nums[i - 1] * nums[j + 1] + \
                        f[i][k - 1] + f[k + 1][j]   # k+1, j没算过啊
                    ans = max(ans, cur)                    
                f[i][j] = ans
                # list comprehension快得多
                # f[i][j] = max([nums[k] * nums[i - 1] * nums[j + 1] + \
                #         f[i][k - 1] + f[k + 1][j] for k in xrange(j, i - 1, -1)])
        return f[1][N - 2]

if __name__ == '__main__':
    """
    题设: 
        n个气球. 每炸一个加上 nums[left] * nums[i] * nums[right]
        求最大值. nums[-1] = nums[n] = 1
        0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
    解法1: 记忆化搜索  872 ms
        状态: f[i][j] 表示所有i, j之间的爆炸方法, 属性是最大值.
        状态转移: 
            k如果表示第一个pop出的元素:
                f[i][j] = max(n[k]*n[k-1]*n[k+1] + f[i][k-1] + f[k+1][j])
                但是这样的话递归的两个分支f[i][k-1]就必须越过k这个数, 很难实现
            k表示当前最后pop的元素: 
                f[i][j] = max(n[k]*n[i-1]*n[j+1] + f[i][k-1] + f[k+1][j])
                可以实现. 
        初始化: 两边加sentinel
        返回值: 1,N区间的最大值
    解法2: DP  332ms
        这题应该是穷举, 所以DP还是更快. 
        区间DP有两种循环方式:
            1. 外层循环区间长度, 内层start位置
            2. 外层循环j, 内层循环当前i, 内环需要从右向左. 
        感觉第二种做法更好写更好想. 而且因为locality也更快. 最快的答案也是如此.
        含义:
            是随着j的增加, [0, i]的情况不变, 
            所以每次只需要求区间[i, j]的情况. 因为j是新加入的, 需要从后向前循环.
    解法3: 
        最快的答案是变掉了dp的定义? 不管了.
    """
    s = Solution()
    print(s.maxCoins([3,1,5,8]))
    print(s.maxCoins([2]))
    print(s.maxCoins([2, 3]))
# @lc code=end

