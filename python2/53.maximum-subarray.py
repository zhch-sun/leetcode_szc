#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
class Solution(object):
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     localV = float('-inf')
    #     globalV = float('-inf')
    #     for n in nums:
    #         localV = n + max(localV, 0)
    #         globalV = max(globalV, localV)
    #     return globalV

    def maxSubArray(self, nums):
        psum = 0
        curMin = 0  # Note 不能初始化成float('inf'), 实际是N+1的第一位!
        ans = float('-inf')
        for n in nums:
            psum += n
            ans = max(ans, psum - curMin)  # Note 和下面顺序不能调换
            curMin = min(curMin, psum)
        return ans
    
    # def maxSub(self, nums, l, r):
    #     if l > r:
    #         return float('-inf')
    #     elif l == r:
    #         return nums[l]
    #     mid = l + (r - l) / 2  # mid in [l, r]因为向下取整,所以mid可能一直是l 导致死循环
    #     left_max = self.maxSub(nums, l, mid - 1)  # must be m-1!
    #     right_max = self.maxSub(nums, mid + 1, r)
    #     center = self.maxCenter(nums, l, r)
    #     return max(left_max, right_max, center)

    # def maxCenter(self, nums, l, r):
    #     mid = l + (r - l) / 2
    #     res = nums[mid]
    #     cur = res
    #     for i in range(mid-1, l-1, -1):
    #         cur += nums[i]
    #         res = max(cur, res)
    #         # if cur > res:
    #             # res = cur
    #     cur = res  # current left max
    #     for i in range(mid+1, r+1, 1):
    #         cur += nums[i]
    #         res = max(cur, res)
    #     return res

    # def maxSubArray(self, nums):
    #     if not nums:
    #         return 0
    #     return self.maxSub(nums, 0, len(nums) - 1)

if __name__ == '__main__':
    """
    题设: 找到和最大的连续子序列, 返回和. 正负数. 
    解法1 动态规划:
        状态: 集合: 以i为结尾的所有子序列, 属性: 最大值f[i]
        状态转移: i->i+1. 
            一定含有A[i+1]这个值. 
            如果f[i]>0, 则加上f[i], 反之只有A[i+1]自己
        返回值: 所有状态中的最大值. 
    解法3: psum法
        psum: 维护过程中的最小的psum值, 和每个psum比较即可.
    解法2 分治法
        答案: https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
    """
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
