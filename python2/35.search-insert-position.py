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
            low = mid + 1  # note the +1 (必须+1 否则死循环)
        else:
            high = mid - 1  # note the -1 (必须-1 否则死循环)
    return None  #note this one!

class Solution(object):
    # def searchInsert(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """       
    #     import bisect
    #     return bisect.bisect_left(nums, target)
    #     import bisect
    #     return bisect.bisect_right(nums, target)

    def searchInsert(self, nums, target):
        # 标准库 bisect_left
        lo, hi = 0, len(nums)
        while lo < hi:  # 不变量: [lo, hi]; 循环结束条件是lo = hi
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:  # Note, 循环不会遇到nums[hi]的情况. 
                lo = mid + 1  # 必须加一是因为解一定在[lo + 1, hi]里面
            else:
                hi = mid  # 不-1因为会违背不变量, 即包含>=的情况
        return lo

    # def searchInsert(self, nums, target):
    #     # 标准库bisect_right
    #     lo, hi = 0, len(nums)
    #     while lo < hi: 
    #         mid = lo + (hi - lo) // 2
    #         if nums[mid] <= target:  # 也是添加一个=号
    #             lo = mid + 1
    #         else:
    #             hi = mid
    #     return lo

    # def searchInsert(self, nums, target):
    #     # 我的bisect_left: 如果有多个重复值, 会插入到最左边
    #     # 这个解法可以推广到bisect_right. 比标准库更好理解.
    #     # 根据初始化解一定在[low, high+1]之间
    #     lo = 0  # even works with [] input
    #     hi = len(nums) - 1
    #     # 循环不变量: 循环保证解依旧在[low, high+1]之间. 甚至跳出循环依旧保证!
    #     # 为什么一定要 +1 -1: -1是保证循环不变量? +1是因为rounding lo和hi相邻时会死循环在lo上. 
    #     while lo <= hi:  # note the <=
    #         mid = lo + (hi - lo) // 2  # overflow bug and //
    #         if nums[mid] < target:  # 改成<=变成bisect_right
    #             lo = mid + 1   # 保证解>= low (必须同时+1和-1 否则死循环, 原因是最后找错了位置死循环)
    #         else:  # nums[mid] >= target
    #             hi = mid - 1  # the solution <= high + 1
    #     return lo

    # def searchInsert(self, nums, target):
    #     # 我的bisect_right: 如果有多个重复值, 会插入到最右边
    #     # 其实是返回大于target的最小值的位置, 解依旧在[low, high+1]
    #     lo = 0
    #     hi = len(nums) - 1
    #     while lo <= hi:  # note the <=
    #         mid = lo + (hi - lo) // 2  # overflow bug and //
    #         if nums[mid] <= target:  # 改成<=变成bisect_right
    #             lo = mid + 1   # 保证解>= low (必须同时+1和-1 否则死循环, 原因是最后找错了位置死循环)
    #         else:  # nums[mid] >= target
    #             hi = mid - 1  # the solution <= high + 1
    #     import bisect
    #     if bisect.bisect_right(nums, target) != lo:
    #         raise Exception("wrong results of my bisect_right")
    #     return lo

    # def searchInsert(self, nums, target):
    #     # search target所在的一个区间
    #     # 根据初始化解一定在[low, high+1]之间
    #     import bisect
    #     low = 0
    #     high = len(nums) - 1
    #     while low <= high:
    #         mid = low + (high - low) // 2
    #         if nums[mid] < target:
    #             low = mid + 1
    #         elif nums[mid] > target:
    #             high = mid - 1
    #         else: 
    #             low = bisect.bisect_left(nums, target, low, mid)
    #             high = bisect.bisect_right(nums, target, mid, high)
    #             return low, high - 1 # high-1 because the return of bisect_right
    #     return low, high + 1  # low == high+1


if __name__ == '__main__':
    """
    刷题发现标准库的解法更加通用. 
    标准库的情况(都在针对找一个位置插入数): 
    task1: bisect_left
    task2: bisect_right, 
    区别在于: 如果有同样大小的数选择左边插还是右边插. 多个同样大小的数同理. 
    注意: left的需要返回找到数的index, right需要返回index+1
    标准库源码 https://github.com/python/cpython/blob/master/Lib/bisect.py

    task3: 和bisect_left非常相似, 只是出现多个的时候返回最右边的. 这个自己在if中加一个条件
    task4: return 返回满足条件的数的范围: 我自己的解法 
    可以线性查找; 可以跑两遍标准库; 第二次标准库可以用第一次的结果进行加速, 如stackoverflow.
    https://stackoverflow.com/questions/30794533/how-to-do-a-binary-search-for-a-range-of-the-same-value
    我自己的做法应该是理论最快?
    """
    s = Solution()

    print(s.searchInsert([1,2,5,6], 5))
    print(s.searchInsert([1,2,5,6], 2))
    print(s.searchInsert([1,2,5,6], 3))
    print(s.searchInsert([1,2,5,6], 7))
    print(s.searchInsert([1,2,5,6], 0))
    print(s.searchInsert([1,2,5,5,5,5,6,7], 5))
    print(s.searchInsert([1,2,5,5,6,7], 5))
    print(s.searchInsert([1,2,5,6], 1))
    print(s.searchInsert([1,2,5,6], 6))
    print(s.searchInsert([6], 6))
    print(s.searchInsert([], 0))


