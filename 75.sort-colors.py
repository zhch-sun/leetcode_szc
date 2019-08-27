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
        # [0, i) [i, k) [k, j] (j, N-1]        
        i, k, j = 0, 0, len(nums) - 1
        while k <= j:  # [k,j]之间不确定
            if nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
                i += 1
            elif nums[k] == 1:
                k += 1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1  # Note k
        
if __name__ == '__main__':
    """
    荷兰国旗问题, 类似3way quicksort. 三个指针. 
    [0, i) < v; [i, k) == v; (j, N-1] < v; [k, j]是不确定
    结束条件应该只能是j. 
    """
    s = Solution()
    print(s.sortColors([2,0,2,1,1,0,1,1,1]))
