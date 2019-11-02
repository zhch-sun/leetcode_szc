#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
class Solution(object):
    # def maxSubArray(self, nums):
    #     for i in range(1, len(nums)):
    #         if nums[i-1] > 0:
    #             nums[i] += nums[i-1]
    #     return max(nums)  
    #   
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # two 1.: max val ending with current pos i 2. containing max with all ending position
    #     # state i means the result suppose the array ending position is i 
    #     if not nums:
    #         return 0
        
    #     local_max = nums[0]  # note tgiglhis should be long 
    #     global_max = nums[0]  # TODO python's number float('-inf') float('inf')
    #     for cur in nums[1:]:
    #         # critical part! either just cur pos or prev + cur; 
    #         # 关键不在于i的正负, 而在于之前local_max的正负, 如果是负则不用加! 正加!
    #         # local_max = local_max + cur if local_max > 0 else cur
    #         local_max = max(cur, local_max + cur)
    #         global_max = max(global_max, local_max)
        
    #     return global_max
    
    def maxSub(self, nums, l, r):
        if l > r:
            return float('-inf')
        elif l == r:
            return nums[l]
        mid = l + (r - l) / 2  # mid in [l, r]因为向下取整,所以mid可能一直是l 导致死循环
        left_max = self.maxSub(nums, l, mid - 1)  # must be m-1!
        right_max = self.maxSub(nums, mid + 1, r)
        center = self.maxCenter(nums, l, r)
        return max(left_max, right_max, center)

    def maxCenter(self, nums, l, r):
        mid = l + (r - l) / 2
        res = nums[mid]
        cur = res
        for i in range(mid-1, l-1, -1):
            cur += nums[i]
            res = max(cur, res)
            # if cur > res:
                # res = cur
        cur = res  # current left max
        for i in range(mid+1, r+1, 1):
            cur += nums[i]
            res = max(cur, res)
        return res

    def maxSubArray(self, nums):
        if not nums:
            return 0
        return self.maxSub(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    """
    动态规划:
    解释 https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
    分成了两步, 一个是ending i的最小值, 一个是假设序列0-i的最小值, 两个阶段? 
    可以用nums来存global max, 这样可以省下O(n)的空间
    
    分治法答案: https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
    """
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
