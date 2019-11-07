# -*- coding: utf-8 -*- 

#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#
class Solution(object):
    # def canPartition(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """        
    #     total = sum(nums)
    #     if total & 1:
    #         return False
    #     total /= 2
    #     # 二维矩阵长度都要加1
    #     f = [[False] * (total + 1)  for _ in xrange(len(nums) + 1)]
    #     # Note 所有行的第一列, 表示不选item和为0, 都必须True
    #     for i in xrange(len(nums)):
    #         f[i][0] = True
    #     # Note 这里用了start=1! 注意循环变量与f内索引的关系. 
    #     for i, n in enumerate(nums, start=1):
    #         for j in xrange(n, total + 1):  # Note 到n-1
    #             f[i][j] = f[i - 1][j] | f[i - 1][j - n]
    #     return f[-1][-1]

    # def canPartition(self, nums):
    #     total = sum(nums)
    #     if total & 1:
    #         return False
    #     total /= 2
    #     f = [False] * (total + 1)  
    #     f[0] = True  # 初始化! 0个物体
    #     for n in nums:
    #         for j in xrange(total, n - 1, -1):  # Note 到n-1
    #             f[j] = f[j] | f[j - n]
    #     return f[-1]

    # def canPartition(self, nums):
    #     total = sum(nums)
    #     if total & 1:
    #         return False
    #     total /= 2
    #     f = [False] * (total + 1)  
    #     f[0] = True  # 初始化! 0个物体
    #     curSum = 0
    #     for n in nums:
    #         curSum += n  # 避免可以不sum子数组
    #         for j in xrange(min(total, curSum), n - 1, -1):  
    #             f[j] = f[j] | f[j - n]
    #         if f[-1]:
    #             return True  # 224ms
    #     return False

    def canPartition(self, nums):
        # bits解法, 类似素数筛法
        # 是DP的一种直观理解方式. 
        total = sum(nums)
        if total & 1:
            return False
        half = total >> 1  # 右移代替除2
        bits = 1  # Note 初始化!!!
        for n in nums:
            bits |= bits << n
            # if (bits >> half) & 1 == 1:  # 只能加上==1, bits前面若干位可能=1
            if bits & (1 << half):  # 厉害了, 1<<half=00010000
                return True  # early stopping
        return False

    # def canPartition(self, nums):
    #     def dfs(idx, targets):
    #         if idx >= N:  # 由题意可以省去这个判断.
    #             return False
    #         for i in (0, 1):
    #             if targets[i] >= nums[idx]:
    #                 targets[i] -= nums[idx]
    #                 if targets[i] == 0 or dfs(idx + 1, targets):
    #                     return True
    #                 targets[i] += nums[idx]
    #         return False
        
    #     N = len(nums)
    #     total = sum(nums)
    #     if total & 1:
    #         return False
    #     half = total >> 1
    #     nums.sort(reverse=True)
    #     return dfs(0, [half, half])

if __name__ == '__main__':
    """
    题设: 数组非空且只是正数. 
    分析: 
        DP: 这题cost是sum, value是能否组成 
        没有求最大值, 所以可以有dfs或者O(N)解法
        TODO: 
            1. 理解必须是正数?
            2. 和target sum的关系? 与subset sum 相似? 
            3  dfs的复杂度是O(2^(n/2))? 因为early stopping所以快?
    解法1: O(N2)
        状态: 前i个数能凑出和为j的情况
        转移公式:
            f[i][j] = max(f[i-1][j], f[i-1][j-c[i]] + v[i])
        建模: 
            属于变体里面找特定的背包空间的题目. 
        坑:
            1. 矩阵长宽都要+1
            2. 初始化要初始所有行的第一列...
            3. 循环时start=1
    解法2: O(N2)
        转移公式: f[j] = max(f[j], f[j-c[i] + v[i]])
    解法3: 
        01背包两个常数优化 
        0. 默认速度: 834ms
        1. 内循环范围: 600ms
        2. early stopping: 236ms
    解法4: O(N) 20ms
        二进制做法, 把dp内循环变成bits右移和或操作. 
        bits的从右向左第j位代表是否前i个数是否能组成和为j. 
        这个解法对DP理解的启发:
            根据这个解法, 内层循环也可以找到之前所有不为False的j, 加上当前item
            但是如果从前向后循环, 会加两次, 所以还是需要从后向前找. 
        直观理解: 
            完全是素数筛法. 因为实际上是把相应每次右移num的位置, 
            而不是每隔c的距离搞事情. 
        坑: 
            1. 初始化. 
            2. check某一位是否为1的方法
    解法5: O(2^n) 带有启发性, 所以更快.
        sort + dfs(backtrack)
        sort的结果是从大到小的, dfs时先考虑大的, 从这个角度来讲是启发式的, 会快
        用[half, half]代表dfs的两条支路. 
    """
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))
    print(s.canPartition([1, 2, 3, 5]))
    print(s.canPartition([1, 2, 5]))

