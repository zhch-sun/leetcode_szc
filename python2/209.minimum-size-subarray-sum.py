#
# @lc app=leetcode id=209 lang=python
#
# [209] Minimum Size Subarray Sum
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        total = 0
        res = float('inf')
        lo = 0
        for hi, item in enumerate(nums, start=1):  # [lo, hi)
            total += item
            while total >= s:
                res = min(res, hi - lo)
                total -= nums[lo]
                lo += 1
        return res if res != float('inf') else 0

    # def minSubArrayLen(self, s, nums):
    #     if not nums:
    #         return 0
        
    #     lo, hi = 0, 0
    #     cur, res = 0, float('inf')
    #     while hi < len(nums):  # Note 注意<=
    #         hi += 1
    #         cur += nums[hi - 1]
    #         while cur >= s:
    #             res = min(res, hi - lo)
    #             cur -= nums[lo]
    #             lo += 1
    #     return 0 if res == float('inf') else res

if __name__ == '__main__':
    """
    题设: 
        给定一个含有n个正整数的数组和一个正整数s ，
        找出该数组中满足其和 ≥s 的长度最小的连续子数组。不存在返回0。
        76题进阶版, 151题 三指针 TODO 560题: 这题存在负数, 不能指针!
    坑: 不能用res is float('inf')
    解法1: 
        双指针. 
        还有一种写法是用for循环. 因为这个循环每次hi+1, 所以hi可以当for的index???
    解法2: 
        二分查找O(nlogn). 复杂不写. 
        先求出cumsum, 再对每一个其实位置通过cumsum二分找结束点: 复杂不写
    """
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
