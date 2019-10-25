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
        if not nums:
            return -1
        lo, hi = 0, len(nums) - 1
        pivot = nums[0]  # require最前面的nums判断
        while lo <= hi:  # 需要check最后一位
            mid = lo + (hi - lo) // 2
            if (nums[mid] < pivot) == (target < pivot):
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return mid
            elif nums[mid] < target:  # elif target < pivot 也可以
                hi = mid - 1
            else:  # 不可能相等
                lo = mid + 1
        return -1

if __name__ == '__main__':
    """
    题设: 
        有序数列可能在一个位置旋转, 从这个数列中找任意target, 不存在-1
        无重复数字. 
        拓展: 如果是找旋转位置呢? 有点类似153题. 
            首先确定0>-1即有解. 然后二分, 判断条件是
            1. 与pivot比较, 2. i和i+1比较.
    分析: 
        两段上升序列: 左边高比右边高. 81th是follow-up
        这种解法最好理解: 只用nums[0]当做pivot. 
        还有的解法用当前的lo当pivot, 不是那么好分析. 
    坑: 
        nums[0]使得必须判断空输入...
    解法1: 
        只需要target和nums[mid]是否处于同一半区(不用管lo, hi！): 
        原因是循环的内环是通过比较这两个来更新位置的, 在同一半区时mid值可以正确赋值.
        不同半区时比较target和nums[0]的大小, 来更新 lo, hi
        必须有在最上面判断符为<=的时候 必须有+1和-1, 
        当只有右半边的时候(没有pivot), 为什么也对: 
        只有右半边的时候, 这俩必处于同一边. 按照条件也处于同一边. 

    还有一个答案(相对于我的答案没有优势):
    https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14436/Revised-Binary-Search
    """
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 4))
    print(s.search([4,5,6,7,0,1,2], 5))
    print(s.search([4,5,6,7,0,1,2], 2))
    print(s.search([1,3], 2))
