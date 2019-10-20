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
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return map[nums[i]], i
        return -1, -1


if __name__ == '__main__':
    """
    是否排好序都是o（n），只不过没排序需要o（n）的额外空间
    solutions:
    1. for i for j and compare
    2. build hash for each word, then loop
    3. build hash and compare in the loop at the same time
    """
    s = Solution()        
    out = s.twoSum([2,7,11,15], 22)
    print(out)

