#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
        memo = {}
        for i, n in enumerate(nums):
            if target - n in memo:
                return memo[target - n], i
            memo[n] = i
        return -1, -1

if __name__ == '__main__':
    """
    题设: 元素各不相同
    是否排好序都是o（n），只不过没排序需要o（n）的额外空间
    solutions:
    1. for i for j and compare
    2. build hash for each word, then loop
    3. build hash and compare in the loop at the same time
    """
    s = Solution()        
    out = s.twoSum([2,7,11,15], 22)
    print(out)

