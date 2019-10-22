#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#
import operator
class Solution(object):
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     res = 0
    #     for item in nums:
    #         res = res ^ item
    #     return res
        
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)
    
    # def singleNumber(self, nums):
    #     return 2* sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    """
    题设: 一堆整数全都出现两次, 只有一个出现一次. 找出它. O(1)空间
    解法1: 类似two sum, 用dict/counter记录
    解法2: 用亦或 ^ operator.xor (不一样的时候为1, 一样的时候为0)
    解法3: ^ 和 reduce
    解法4: 数学大法: 求2*set(nums) - sum(nums): 注意这个linear memory.
    """
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))
