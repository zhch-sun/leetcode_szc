#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:  # note the <=
        mid = low + (high - low) // 2  # note //
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1  # note the +1
        else:
            high = mid - 1  # note the -1
    return mid  #note this one!


class Solution(object):
    # def searchInsert(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """       
    #     import bisect
    #     return bisect.bisect_left(nums, target)

    def searchInsert(self, nums, target):
        # 根据初始化解一定在[low, high+1]之间
        low = 0
        high = len(nums) - 1
        # 循环不变量: 循环保证解依旧在[low, high+1]之间. 甚至跳出循环依旧保证!
        while low <= high:  # note the <=
            mid = low + (high - low) // 2  # overflow bug and //
            if nums[mid] < target:
                low = mid + 1  # 保证解>= low
            else:  # nums[mid] >= target
                high = mid - 1  # the solution <= high + 1
        return low  # Wow


if __name__ == '__main__':
    """
    just modify binary search, return low in the end...
    当target大于所有数时, low在结束前会比high大1... 
    当target小于所有数时, high在结束前会变成-1, 即比low小1
    """
    s = Solution()
    print(s.searchInsert([1,2,5,6], 5))
    print(s.searchInsert([1,2,5,6], 2))
    print(s.searchInsert([1,2,5,6], 7))
    print(s.searchInsert([1,2,5,6], 0))


