#
# @lc app=leetcode id=137 lang=python
#
# [137] Single Number II
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 99.9
        stotal = sum(set(nums)) * 3
        return (stotal - sum(nums)) // 2

if __name__ == '__main__':
    """
    没有人考bit, 写正常的O(n)答案
    """
    s = Solution()
    print(s.singleNumber([2,2,3,2]))
    print(s.singleNumber([0,1,0,1,0,1,99]))


