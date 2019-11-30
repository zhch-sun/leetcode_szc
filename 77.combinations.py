#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
from itertools import combinations

class Solution(object):
    def combine(self, n, k):
        return list(combinations(range(1, n + 1), k))

    # def combine(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: List[List[int]]
    #     """        
    #     ans = [[]]  # 这个初始化. 
    #     for _ in xrange(k):
    #         tmp = []
    #         for item in ans:
    #             # 下面这个比判断是否 i > item[-1]更快
    #             start = item[-1] + 1 if item else 1  # 这个加速!!!
    #             tmp += [item + [i] for i in xrange(start, n + 1)]
    #         ans = tmp
    #     return ans

    # def combine(self, n, k):
    #     def dfs(tmp, idx):
    #         if len(tmp) == k:
    #             ans.append(tmp[:])
    #             return
    #         for i in xrange(idx, n + 1):
    #             tmp.append(i)
    #             dfs(tmp, i + 1)  # Note i + 1 !!!
    #             tmp.pop()
    #         return

    #     ans = []
    #     dfs([], 1)
    #     return ans

if __name__ == '__main__':
    """
    题设: 给定n, k, 生成所有组合; k隐含得必须小于等于n
    解法0: 库函数
    解法1: 
        循环, 第一次放所有数, 第二次放比前面都大的
    解法2:
        这种生成所有的题, backtrack是标准答案呀, 而且比循环快?
    """
    s = Solution()
    print(s.combine(4, 2))
