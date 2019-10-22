#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#
class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # 可以认为是错解，标准解法双指针
    #     count = 0
    #     n = len(nums)
    #     for i in range(1, n):
    #         if nums[i-1] == nums[i]:
    #             count += 1
    #         else:
    #             nums[i-count] = nums[i]
    #     return n - count

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0  # start指向待修改位置
        for i in range(1, len(nums)): # 从1开始
            if nums[i] != nums[i-1]:
                start += 1
                nums[start] = nums[i]
        return start + 1  # TODO start应该可以初始化成1？

if __name__ == '__main__':
    """
    题设：
        inplace remove。list后面不care. 80题是follow-up
        这题应该不需要排好序, 只需要同样的数在一起即可
        TODO 应该像80题一样, 直接for循环而不是用idx即可. 
        TODO 根据80题start指向将要赋值的位置
    解法: 
        双指针。外层i内层start
    """
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
