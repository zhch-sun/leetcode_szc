#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
class Solution(object):
    # def maxArea(self, nums):
    #     l = 0
    #     r = len(nums) - 1
    #     volume = 0
    #     while l < r:
    #         h = min(nums[l], nums[r])
    #         volume = max((r - l) * h, volume)
    #         if nums[l] < nums[r]:
    #             l += 1
    #         else:
    #             r -= 1
    #     return volume   
        
    def maxArea(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        volume = 0
        while l < r:
            h = min(nums[l], nums[r])
            volume = max((r - l) * h, volume)
            while nums[l] <= h and l < r:
                l += 1
            while nums[r] <= h and l < r:
                r -= 1
        return volume

if __name__ == '__main__':
    """
    第一种解法很容易理解是正确的. 最终的解一定在两边之内. 
    而且解一定要替代掉当前的短边, 否则一定小于当前解. 然后迭代即可. 
    两边相等时, 两个边必须都被替换掉!
    所以第二种解法就隐式得做了这一点! 如果两边 <= h, 都移动. 
    正常情况其实是一个为h, 另一个大于h的!
    """
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))

