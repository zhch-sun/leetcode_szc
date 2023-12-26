#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#
class Solution(object):
    def searchRange(self, nums, target):
        # 模板1
        def bisect_left(nums, target, lo=None, hi=None):
            lo = 0 if not lo else lo
            hi = len(nums) if not hi else hi
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def bisect_right(nums, target, lo=None, hi=None):
            lo = 0 if not lo else lo
            hi = len(nums) if not hi else hi
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        # import bisect
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = bisect_left(nums, target, lo, mid)
                hi = bisect_right(nums, target, mid, hi+1)  # 注意hi+1
                # lo = bisect.bisect_left(nums, target, lo, mid)
                # hi = bisect.bisect_right(nums, target, mid, hi+1)
                return [lo, hi-1]  # Note this -1!!!!
        return [-1, -1]

        # left = bisect_left(nums, target)
        # right = bisect_right(nums, target) - 1
        # return [left, right] if left <= right else [-1, -1]

    # def searchRange(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     # 模板二
    #     def bisect_left(nums, target, lo, hi):
    #         while lo <= hi:
    #             mid = (hi - lo) // 2 + lo
    #             if nums[mid] < target:
    #                 lo = mid + 1
    #             else:
    #                 hi = mid - 1
    #         return lo
        
    #     def bisect_right(nums, target, lo, hi):
    #         while lo <= hi:
    #             mid = (hi - lo) // 2 + lo
    #             if nums[mid] <= target:
    #                 lo = mid + 1
    #             else:
    #                 hi = mid - 1
    #         return lo
    #     left = 0
    #     right = len(nums) - 1
    #     while left <= right:
    #         mid = (right - left) // 2 + left
    #         if nums[mid] < target:
    #             left = mid + 1
    #         elif nums[mid] > target:
    #             right = mid - 1
    #         else:
    #             left = bisect_left(nums, target, left, mid)
    #             right = bisect_right(nums, target, mid, right)
    #             return [left, right-1]  # Note this -1!!!!
    #     return [-1, -1]
       
    #     # left = bisect_left(nums, target, 0, len(nums) - 1)
    #     # right = bisect_right(nums, target, left, len(nums) - 1) - 1  # 这里-1！
    #     # return [left, right] if left <= right else [-1, -1]

    

if __name__ == '__main__':
    """
    见35题
    解法1:
        理论最快, 而且有实质的early stopping.
        先二分判断区间, 再分别调用. 
        这题主循环必须用模板二 <=, 因为需要check最后一个值. 
        内层仍然可以用模板一, 但是hi要+1, 这也是标准库的调用方式
        hi+1的调用方式也是和标准库的调用一致的. 所以必须掌握. 
    解法2:
        注意最后的left<=right条件
    解法3:
        解法2可以再尝试early stoppin, 但是实现比较难, 不管了
        1. 需要处理空输入
        2. 为我搜出来的是插入位置, 不能直接索引数组, 可能越界
    """
    s = Solution()
    # print(s.searchRange([5,7,7,8,8,10], 8))
    print(s.searchRange([2,2], 2))
    print(s.searchRange([2,2], 3))
    print(s.searchRange([], 2))

