#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]  # or count=0 major=None
        count = 1
        for i in range(1, len(nums)):
            if count + i - len(nums) > 0:  # my condition for terminate
                return major 
            item = nums[i]
            if item == major:
                count += 1
            elif count > 0:
                count -= 1
            else:
                major = item
        return major


if __name__ == '__main__':
    """
    1. 可以sort取中值. 
    2. 摩尔投票法: 对拼消耗. 每次从序列中挑出两个不同的数字抵消掉. 剩下的就是
    """
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))
