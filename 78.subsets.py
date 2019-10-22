#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        tmp = []
        self.dfs(nums, res, tmp, 0)
        return res

    def dfs(self, nums, res, tmp, pos):
        res.append(tmp[:])
        for i in xrange(pos, len(nums)):
            tmp.append(nums[i])
            self.dfs(nums, res, tmp, i + 1)
            tmp.pop()

if __name__ == '__main__':
    """
    题设:
        给定一堆独立数, 返回其幂集. power set. 即所有可能的情况, 包含[]
        90题 follow
    思路:
        也是一种组合. 组合的特性就是可以记录位置, dfs只搞位置之后的. 
        和combination题一样
    解法1: backtrack
    解法2: TODO iterative: 和permutation差不多. 一个一个元素添加上去. 其实就是BFS. 
    解法3: bit操作就不管了. 
    """
    s = Solution()
    print(s.subsets([1,2,3]))
