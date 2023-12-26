#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
import itertools
from collections import OrderedDict 
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        def dfs(tmp):
            if len(tmp) == N:
                ans.append(tmp[:])  # Note 又忘了..
                return
            for i in xrange(N):
                if not used[i]:
                    tmp.append(nums[i])
                    used[i] = True
                    dfs(tmp)
                    tmp.pop()
                    used[i] = False
            return

        N = len(nums)  # 不需要判断空
        used = [False] * N  # state for used
        ans = []
        dfs([])  # 也可nums转换成set, 这样就没有顺序了.
        return ans

    # def permute(self, nums):
    #     def dfs(tmp):
    #         if len(tmp) == N:
    #             ans.append(list(tmp.keys()))  # Note 又忘了..
    #             return
    #         for n in nums:
    #             if n not in tmp:
    #                 tmp[n] = None
    #                 dfs(tmp)
    #                 tmp.pop(n)
    #         return

    #     N = len(nums)
    #     ans = []
    #     dfs(OrderedDict())  # 也可nums转换成set, 这样就没有顺序了.
    #     return ans

    # def permute(self, nums):
    #     # swap
    #     def helper(nums, begin, res):
    #         # permute begin: end
    #         # [0: begin-1] has been permuted
    #         if begin >= len(nums):
    #             res.append(nums[:])  # Note nums[:]...
    #         for i in range(begin, len(nums)):
    #             nums[begin] , nums[i] = nums[i], nums[begin]
    #             helper(nums, begin + 1, res)  # Note! begin + 1 not i
    #             nums[begin] , nums[i] = nums[i], nums[begin]

    #     res = []
    #     helper(nums, 0, res)
    #     return res

    # def permute(self, nums):
    #     # 枚举每个数放到哪个位置上.
    #     ans = [[]]
    #     for num in nums:
    #         new_res = []
    #         for l in ans:
    #             for i in xrange(len(l) + 1):  # 这里逆序顺序就正常了？
    #                 new_res.append(l[:i] + [num] + l[i:])  # 也可以直接insert()
    #         ans = new_res
    #     return ans if nums else []

    # def permute(self, nums):
    #     def dfs(tmp, u):
    #         if u == N:
    #             ans.append(tmp[:])
    #             return
    #         for i in xrange(N):  # i是path的idx, u是nums的idx
    #             if not used[i]:  # 这时used表示的是tmp的对应位置是否有数.
    #                 used[i] = True
    #                 tmp[i] = nums[u]
    #                 dfs(tmp, u + 1)
    #                 tmp[i] = None
    #                 used[i] = False
    #         return

    #     N = len(nums)
    #     nums.sort()
    #     tmp = [None] * N
    #     used = [False] * N
    #     ans = []
    #     dfs(tmp, 0)
    #     return ans

if __name__ == '__main__':
    """
    题设:
        数字各不相同, 枚举排列的情况.
    两种顺序:
        就是外层循环不一样, 1是循环位置, 2是循环数.
        1. 枚举每个位置上放哪个数, 字典序: 位置1放1,2,3
        2. 枚举每个数放到哪个位置上. 1在第一个位置上, 1在第二个位置上?
    解法1:
        回溯. nary_tree.
        四种除重方法:
            通过state array记录是否用过.
            或者tmp用orderedSet, python没有
            不能保证字典序: 把nums转成set最快. 自动剪枝
            保证字典序: nums转成红黑树应该最快
    解法2:
        ordereddict
    解法3:
        不是字典序.
        首先把第一个数和后面所有的数交换, 
        然后递归交换第二个数
    解法4:
        枚举每个数放到哪个位置上! 
        每个dfs输入的是数的idx u, 里面对位置i枚举
        不是字典序
    解法5:
        枚举每个数放到哪个位置上. 动态改变数组长度.
        https://leetcode.com/problems/permutations/discuss/18237/My-AC-simple-iterative-javapython-solution
    """
    s = Solution()
    print(s.permute([1,2,3]))
