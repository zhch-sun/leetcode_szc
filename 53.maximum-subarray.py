#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # two 1.: max val ending with current pos i 2. containing max with all ending position
        # state i means the result suppose the array ending position is i 
        if not nums:
            return 0
        
        local_max = nums[0]
        global_max = nums[0]  # TODO python's number float('-inf') float('inf')
        for cur in nums[1:]:
            # critical part! either just cur pos or prev + cur; 
            # 关键不在于i的正负, 而在于之前local_max的正负, 如果是负则不用加! 正加!
            local_max = local_max + cur if local_max > 0 else cur
            # local_max = max(cur, local_max + cur
            global_max = max(global_max, local_max)
        
        return global_max

if __name__ == '__main__':
    """
    动态规划:
    解释 https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
    分成了两步, 一个是ending i的最小值, 一个是假设序列0-i的最小值, 两个阶段? 
    我的解法更好理解!  
    TODO 分治法...以及其复杂度的计算. (dicussion上也有答案)
    """
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


