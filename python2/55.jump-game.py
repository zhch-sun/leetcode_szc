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
    题目理解:
        一个数列存着向前跳的格数, 问是否能跳到最后
        并不是存着必须跳的格数. 而是最大可以跳的格数. 
        也就是可以跳<=的格数. 
        TODO: 如果是只能跳这么多格数呢..? DP吗?
    题目思路: 
        只需要维护当前最大可以达到的位置. 并确保过程中pos > idx
    我的判断条件不如答案的精简. 
    """
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
