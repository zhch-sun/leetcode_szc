#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#
class Solution(object):
    def removeElement(self, nums, val):
        start = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1
        return start

    # def removeElement(self, nums, val):
    #     # pop居然是实际最快的解法
    #     while val in nums:
    #         nums.pop(nums.index(val))
    #     return len(nums)

    # def removeElement(self, nums, val):
    #     # filter is a possible way: have to be nums[:], otherwise nums is not changed!
    #     nums[:] = filter(lambda x: x != val, nums)
    #     return len(nums)
    #     # list comprehension use extra space
    #     # return len([x for x in nums if x!=val])
 
if __name__ == '__main__':
    """
    用start是最简单的做法?
    pop的做法应该是更慢的, 但是实际跑出来还是比循环快... 应该是因为while循环次数更少
    还可以用filter或者list comprehension, 但是这样需要额外的空间
    """
    s = Solution()
    # nums = [2,3,5,3,4,4,7]
    # res = s.removeElement(nums, 4)
    nums = [3,2,2,3]
    res = s.removeElement(nums, 3)
    print(res, nums)
    
