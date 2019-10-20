#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#
class Solution(object):
    # def permuteUnique(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     # TODO 不理解呀... 为什么要注释掉下面一个swap? 
    #     def helper(nums, res, begin):
    #         if begin >= len(nums):
    #             res.append(nums[:])
    #         for i in xrange(begin, len(nums)):
    #             if i != begin and nums[i] == nums[begin]:
    #                 continue
    #             nums[begin], nums[i] = nums[i], nums[begin]
    #             helper(nums[:], res, begin + 1)
    #             # 加下面这个是错的!!!!
    #             # nums[begin], nums[i] = nums[i], nums[begin]  
    #     res = []
    #     nums.sort()
    #     helper(nums, res, 0)
    #     return res

    def permuteUnique(self, nums):
        res = [[]]
        for i in xrange(len(nums)):
            num = nums[i]
            new_res = []
            for l in res:
                for i in xrange(len(l) + 1):
                    new_res.append(l[:i] + [num] + l[i:])
                    if i < len(l) and num == l[i]:  # 要先插入再判断
                        break
            res = new_res
        return res

if __name__ == '__main__':
    """
    TODO 最高的答案是有used, 需要重新做
    就是第一题的dfs的swap, 如果两个数相等就不swap. 
    
    对于插入法: To handle duplication, just avoid inserting a number AFTER any of its duplicates.
    TODO 这个的理解方法是对称性. 假设123的permute加入一个新的2. ？？？ 又没有理解了？？？
    """
    s = Solution()
    print(s.permuteUnique([1,2,2]))
