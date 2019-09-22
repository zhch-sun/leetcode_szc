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
        if not nums:
            return 0
        
        lo, hi = 0, 0
        cur, res = 0, float('inf')
        while hi < len(nums):  # Note 注意<=
            hi += 1
            cur += nums[hi - 1]
            while cur >= s:
                res = min(res, hi - lo)
                cur -= nums[lo]
                lo += 1
        return 0 if res == float('inf') else res


if __name__ == '__main__':
    """
    简答解法O(n): two pointers
        还有一种写法是用for循环. 因为这个循环每次hi+1, 所以hi可以当for的index. 
    复杂解法O(nlogn): binary search: 
        先求出cumsum, 再对每一个其实位置通过cumsum二分找结束点: 复杂不写
    """
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
        

