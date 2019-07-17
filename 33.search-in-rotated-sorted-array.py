#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) / 2 + left
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            elif target < nums[0]:  # 不在同一个半区的时候肯定值不一样. 
                left = mid + 1
            else:
                right = mid - 1
        return -1

if __name__ == '__main__':
    """
    这种解法最好理解, 只用nums[0]当做pivot. 还有的用left当pivot, 不是那么好分析. 
    必须有在最上面判断符为<=的时候 必须有+1和-1, 
    问题是当只有右半边的时候, 为什么也对? 只有右半边的时候, 这俩必处于同一边. 按照条件也处于同一边. 

    还有一个答案(相对于我的答案没有优势):
    https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14436/Revised-Binary-Search
    """
    s = Solution()
    # print(s.search([4,5,6,7,0,1,2], 4))
    # print(s.search([4,5,6,7,0,1,2], 5))
    # print(s.search([4,5,6,7,0,1,2], 2))
    print(s.search([1,3], 2))
