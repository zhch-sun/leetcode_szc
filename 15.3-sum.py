#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def sortedTwoSum(self, nums, left, target, res):
        l = left
        r = len(nums) - 1
        while l < r:
            cur = nums[l] + nums[r]
            if cur < target:
                l += 1
                # while l < r and nums[l] == nums[l - 1]:  # Not fast
                #     l += 1          
            elif cur > target:
                r -= 1
                # while l < r and nums[r] == nums[r + 1]:  # not fast
                #     r -= 1                
            else:
                res.append([0 - target, nums[l], nums[r]])
                l += 1  # 必须保证至少+1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:  # Note! 因为前面已经+1 
                    l += 1
                while l < r and nums[r] == nums[r + 1]:  # Note！
                    r -= 1                

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 98 %
        nums.sort()
        res = []
        for idx in xrange(len(nums) - 1):  # 应该可以enumerate
            item = nums[idx]
            if nums[idx] > 0:  # TODO pruning: 0可以替换成任意（target+2）//3; 参照4sum
                break
            if idx > 0 and nums[idx] == nums[idx - 1]:  #  2sum间的重复
                continue
            self.sortedTwoSum(nums, idx + 1, -item, res)  # python的负号是可以接一个变量的
        return res

if __name__ == '__main__':
    """
    题设target=0
    注意有 -1, -1, 2这种搭配, 所以不能在最前面搞一个set!!!!(或者sort之后再set))
    思路1 sort之后每个元素来, 剩下的两个元素就是一个sorted 2sum.
        167th是sorted2sum：用循环不变量证明: 里面可能有多组解
        问题是duplicates, 一个是2sum内的重复, 一个是2sum间的重复（只要去除同一个最小值的重复即可）
    """
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

