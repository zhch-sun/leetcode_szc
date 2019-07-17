#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#
import bisect

class Solution(object):
    # def findMin(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # 70%
    #     if not nums:
    #         return None
    #     left, right = 0, len(nums) - 1
    #     # 这题的循环不变量只能在[left, right]之间, 不是插入位置那道题了..
    #     # 这样结束的时候是left==right
    #     while left < right:
    #         if nums[left] < nums[right]:
    #             return nums[left]
    #         mid = (right - left) // 2 + left
    #         # mid + 1 可能不存在呀? 
    #         if nums[mid] >= nums[0]:  # 也可以是nums[mid] >= nums[left]
    #             # 因为向下取整 所以left = right-1的时候一定掉到这里去. 
    #             left = mid + 1  # 循环不变量: [left, right] mid+1一定存在
    #         else:
    #             right = mid  # -1会违背循环不变量
    #     return nums[left]

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 89%
        if not nums:
            return None
        left, right = 0, len(nums) - 1
        # 循环不变量只能在[left, right]
        # 这样结束的时候是left==right
        # 因为向下取整所以mid不会等于nums[-1]
        while left < right:
            # if nums[left] < nums[right]:  # slower
            #     return nums[left]        
            mid = (right - left) // 2 + left
            if nums[mid] > nums[-1]:  # 也可以是nums[mid] >= nums[left]
                left = mid + 1  # 循环不变量: [left, right] mid+1一定存在
            else:  # nums[mid] < nums[-1] 不会相等. 
                right = mid  # -1会违背循环不变量
        return nums[left]
        

if __name__ == '__main__':
    """
    TODO 需要写find maximum. 
    必须用nums[-1]的原因是, 需要处理只有后半段的情况(解一定在后半段). 
    宝宝的做法是用梯度? 这样的化每次要处理四个数还有边界条件? 比较复杂? 
    """
    s = Solution()
    # print(s.findMin([3,4,5,1,2]))
    print(s.findMin([3,1,2]))
    # print(s.findMin([1]))
    print(s.findMin([1,2]))
    # print(s.findMin([]))
