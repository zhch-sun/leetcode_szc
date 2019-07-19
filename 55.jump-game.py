#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pos = 0
        for idx, item in enumerate(nums):
            if idx > pos:
                return False
            pos = max(pos, idx + item)
            # if pos == idx and idx != len(nums) - 1:
            #     return False
        return True

if __name__ == '__main__':
    """
    注意数组下标, 也可以从后向前? 但是应该不如我快. 
    我的判断条件不如答案的精简. 
    """
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
