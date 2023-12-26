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
    解法2: 
        注意双指针的初始化, 使得无需空判断!!! 两个指针均在数列之前. 
        这种初始化只有在求最值时才可以, 求个数不可以.
    解法3: 
        双状态数组法
        f[i]: 从前i个数选, 所有不选nums[i]的最大值
        g[i]: 从前i个数选, 所有选nums[i]的最大值
        更复杂但似乎也不general. 
    """
    s = Solution()
    print(s.rob([1,2,3,1]))
    print(s.rob([2,7,9,3,1]))

