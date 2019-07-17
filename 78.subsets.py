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
        # 单独拿出来更快?!
        res.append(tmp[:])
        for i in xrange(pos, len(nums)):
            tmp.append(nums[i])
            self.dfs(nums, res, tmp, i + 1)
            tmp.pop()


if __name__ == '__main__':
    """
    TODO iterative: 和permutation差不错. 一个一个元素添加上去. 其实就是BFS. 
    bit操作就不管了. 
    """
    s = Solution()
    print(s.subsets([1,2,3]))

