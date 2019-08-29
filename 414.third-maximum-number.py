#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#
import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            return heapq.nlargest(3, nums)[-1]

if __name__ == '__main__':
    """
    这个题就是要distinct的number.
    另一个答案是用 红黑树等有序符号表. pyhton里没有...
    """
    s = Solution()
    print(s.thirdMax([3,2,1]))
    print(s.thirdMax([1,2]))
    print(s.thirdMax([2,2,3,1]))
        

