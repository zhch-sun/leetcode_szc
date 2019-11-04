#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#
class Solution(object):
    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """        
    #     if not nums:
    #         return 0
    #     N = len(nums)
    #     f = [0] * (N + 1)
    #     f[0], f[1] = 0, nums[0]
    #     for i in xrange(1, N):
    #         f[i + 1] = max(f[i], f[i - 1] + nums[i])
    #     return f[-1]

    # def rob(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """        
    #     # 无需判断 nums
    #     N = len(nums)
    #     f = [0] * (N + 2)
    #     for i in xrange(N):
    #         f[i + 2] = max(f[i + 1], f[i] + nums[i])
    #     return f[-1]

    def rob(self, nums):
        # if not nums:  # Note 无需判断!!!
        #     return 0
        p0, p1 = 0, 0
        for n in nums:
            cur = max(p1, p0 + n)
            p0, p1 = p1, cur
        return p1

if __name__ == '__main__':
    """
    题设: 
        数列中取数, 不能取相邻的, 求最大和
        数列非负
    解法1: dp数组
    解法2: 注意双指针的初始化, 使得无需空判断!!! 两个指针均在数列之前. 
    """
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))

