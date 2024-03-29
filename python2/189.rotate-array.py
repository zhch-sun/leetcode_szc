#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#
class Solution(object):
    # def rotate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: None Do not return anything, modify nums in-place instead.
    #     """
    #     k %= len(nums)
    #     while k:
    #         nums.insert(0, nums.pop())
    #         k -= 1

    # def rotate(self, nums, k):
    #     # 80 %
    #     k = k % len(nums)
    #     nums[:] = nums[-k:] + nums[:-k]

    def rotate(self, nums, k):
        # 94% 
        def reverse(array, l, r):
            while l < r:
                array[l], array[r] = array[r], array[l]
                l += 1
                r -= 1
        k %= len(nums)  # must use this
        n = len(nums)
        reverse(nums, 0, n - k - 1)
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - 1)
    
    # def rotate(self, nums, k):
    #     # 92.34%
    #     """
    #     1. 简单情况: k < n/2时, 就是一个对调
    #     1 2 3 4 5 6 7
    #     5 6 7 1 2 3 4
    #     2. 复杂情况: k > n/2时, 注意如下的运动pattern. 
    #     1 2 3 4 5 6 7 8 9 10
    #     4 5 6 1 2 3 7 8 9 10
    #     4 5 6 7 8 9 1 2 3 10
    #     其实就是最后的1 2 3 10做了一个对调. 这个对调把1个数调到了最后. 这变成了
    #     个数为n - k个, k = k % (n-k)
    #     """
    #     n = len(nums)  # n is the number
    #     def helper(k, l):  # 不需要 r
    #         k %= (n - l)  # l is also the number
    #         if k != 0:
    #             for i in range(k):
    #                 nums[l + i], nums[n - k + i] = nums[n - k + i], nums[l + i]
    #             l += k
    #             helper(k, l)
    #     helper(k, 0)
    
    # def rotate(self, nums, k):
    #     l = 0
    #     n = len(nums)
    #     k %= (n - l)
    #     while k != 0:
    #         for i in range(k):
    #             nums[l + i], nums[n - k + i] = nums[n - k + i], nums[l + i]
    #         l += k
    #         k %= (n - l)

if __name__ == '__main__':
    """
    题设: 
        给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
        inplace原地解决. 
    注意: 应该先mod出最短要滚动的位置
    解法1: pop然后在0位置insert, 太慢了 
    解法2: slice: 实际用了额外内存. 注意用-k索引.
    解法3: 分别reverse两部分, 再reverse整个. 不知证明? 面试算法. 
    解法4: cyclic算法: 需要仔细可视化, 而且也不cache friendly; 太复杂了.
    """
    s = Solution()
    array = [1,2,3,4,5,6,7]
    s.rotate(array, 3)
    print(array)
