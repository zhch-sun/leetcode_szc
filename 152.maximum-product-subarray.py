#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = float('-inf')
        cur_max = cur_min = 1
        for cur in nums:
            tmp_max = max(cur_max * cur, cur_min * cur, cur)  # 状态转移!
            tmp_min = min(cur_min * cur, cur_max * cur, cur)  # 状态转移!
            cur_max, cur_min = tmp_max, tmp_min
            ans = max(ans, cur_max)
        return ans

if __name__ == '__main__':
    """
    题设: 数列里面正负整数, 求最大连续序列乘积
        类似于53题最大子序列之和. 
    解法:
        以i为结尾的最大值. 最小值, 都有可能取到0; 转移方程忘记max了....
        pos[i] = max(num, pos[i-1] * num if num >= 0 else neg[i-1] * num)
        neg[i] = min(num, neg[i-1] * num if num > 0 else pos[i-1] * num)
        
        优化的转移方程:
        tmp_max = max(cur_max * cur, cur_min * cur, cur)  # 状态转移!
        tmp_min = min(cur_min * cur, cur_max * cur, cur) 
    正确性:
        1. 这俩max完全依赖于cur_min和max, min完全依赖于max和min 
        2. cur_max足够生成global max
        3. cur_max, cur_min均为正, 均为负, 一正一副, 都是对的..
    """
    s = Solution()
    print(s.maxProduct([2,3,-2,4]))
    print(s.maxProduct([-2,0,-1]))
    print(s.maxProduct([-4, -3]))
    # print(s.maxProduct([-1, -2, -9, -6]))
    # print(s.maxProduct([2, -5, -2, -4, 3]))
    # print(s.maxProduct([-2,3,-4]))
    # print(s.maxProduct([-4, -3,-2]))
