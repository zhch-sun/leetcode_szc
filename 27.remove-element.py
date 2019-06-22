#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#
class Solution(object):
    def removeElement(self, nums, val):
        start = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1
        return start

    # def removeElement(self, nums, val):
    #     while val in nums:
    #         nums.pop(nums.index(val))
    #     return len(nums)


if __name__ == '__main__':
    """
    用start是最简单的做法?
    pop的做法应该是更慢的, 但是实际跑出来还是比循环快... 应该是因为while循环次数更少?
    """
    s = Solution()
    nums = [2,3,5,3,4,4,7]
    res = s.removeElement(nums, 4)
    print(res, nums)
    
