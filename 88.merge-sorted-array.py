#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:  # Note do not use i!
            if m >= 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            elif n >= 0:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
    
    # def merge(self, nums1, m, nums2, n):
    #     nums1[m:] = nums2
    #     nums1.sort()


if __name__ == '__main__':
    """
    heap? 需要从后向前搞...  (因为需要从要输出的位置开始循环)
    直接用m和n当做位置指针. 用m+n-1当做当前写的位置, 不需要再搞
    当然也可以加起来sort...  list.sort()是inplace sorted()是return new
    """
    s = Solution()
    print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
