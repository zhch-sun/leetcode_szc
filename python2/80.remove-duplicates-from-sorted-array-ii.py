#
# @lc app=leetcode id=80 lang=python
#
# [80] Remove Duplicates from Sorted Array II
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for item in nums:
            if k < 2 or item > nums[k - 2]:
                nums[k] = item
                k += 1            
        return k

    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = len(nums)
    #     if n <= 2:
    #         return n
    #     k = 2
    #     for i in range(2, n):
    #         if nums[i] > nums[k - 2]:  # 注意这里是nums[i] 与 nums[k-2]比较...
    #             nums[k] = nums[i]
    #             k += 1
    #     return k
        
if __name__ == '__main__':
    """
    题设: 26th是系列的第一题. 仍然inplace, 区别是允许最多重复两次. 
    解法1:
        非常漂亮. 直接比较当前num和以k为计数的前面的值. 且不需要分类讨论
        k指向将要被赋值的位置
    解法2:  
        我的解法.. 是解法1的丑陋版, 不予考虑
    """
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,2,3]))
