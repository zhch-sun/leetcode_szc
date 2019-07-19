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
    下面是我的解法. 注意的是赋值的双方...
    nums[k] = nums[i]
    以及聪明的比较方法: nums[i] > nums[k - 2]
    """
    s = Solution()
    print(s.removeDuplicates([1,1,1,2,2,3]))
