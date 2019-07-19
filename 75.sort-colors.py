#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # next position to write
        i = 0
        j = len(nums) - 1
        k = 0
        while k <= j:  # 结束条件!
            if nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1  # k不加1!!!
            elif nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            else:
                k += 1
        return nums

        
if __name__ == '__main__':
    """
    实际上是三个指针. 需要仔细想清楚指针的移动. 还有结束条件!
    结束条件应该只能是j. 
    """
    s = Solution()
    print(s.sortColors([2,0,2,1,1,0,1,1,1]))
