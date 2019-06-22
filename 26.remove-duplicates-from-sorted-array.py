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
        start = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                start += 1
                nums[start] = nums[i]
        return start + 1

if __name__ == '__main__':
    """
    注意不能用额外的space, 需要修改输入的list, 使得前面是不重复的. list后面不care.
    用start还是比count简单一些. 
    """
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
