#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
import itertools
class Solution(object):
    # def permute(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     def dfs(res, tmp, nums):
    #         if len(tmp) == len(nums):
    #             res.append(tmp[:])  # have to copy here
    #         else:
    #             for item in nums:
    #                 if item in tmp:  # 这里又是o(n)的复杂度...
    #                     continue
    #                 tmp.append(item)
    #                 dfs(res, tmp, nums)
    #                 tmp.pop()
    #     res = []
    #     tmp = []
    #     dfs(res, tmp, nums)
    #     return res

    def permute(self, nums):
        def helper(nums, begin, res):
            # permute begin: end
            # [0: begin-1] has been permuted
            if begin >= len(nums):
                res.append(nums[:])  # Note nums[:]...
            for i in range(begin, len(nums)):
                nums[begin] , nums[i] = nums[i], nums[begin]
                helper(nums, begin + 1, res)  # Note! begin + 1 not i
                nums[begin] , nums[i] = nums[i], nums[begin]

        res = []
        helper(nums, 0, res)
        return res

    # def permute(self, nums):
    #     # 这个顺序很奇怪....
    #     res = [[]]
    #     for num in nums:
    #         new_res = []
    #         for l in res:
    #             for i in range(len(l) + 1):
    #                 new_res.append(l[:i] + [num] + l[i:])
    #         res = new_res
    #     return res

if __name__ == '__main__':
    """
    确实是个dfs，只不过这里不是binary而是n-ary tree。
    backtrack里面需要if item in tmp来判断...有点慢呀这里. 
    dfs可以用swap(第二个答案)，好处是省掉了memcopy的时间。python的答案都有很多memcopy
    但是swap的结果不够好, 是123 132 213 231 321 312. 注意321和312是反着的... 算法就是这样..
    TODO iterative，基础是插入法, 一个一个数字插入. 1只有一个位置, 2有两个, 3有 2*3=6个 4有6*4=64个
    https://leetcode.com/problems/permutations/discuss/18237/My-AC-simple-iterative-javapython-solution
    上面的做法要求copy array, 很慢. 下面用swap解决了这个问题. 生长过程是9*8*7*6*5... 不知道怎么证明, 不搞. 
    https://leetcode.com/problems/permutations/discuss/18378/Simple-python-code-without-recursion
    """
    s = Solution()
    print(s.permute([1,2,3]))
    

