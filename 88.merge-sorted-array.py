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
    题设: 合并nums2到nums1上. nums1空间足够.  
    解法: 
        从前向后需要copy array, 从后向前就trivial可以了..
        维护m和n两个指针, 指向两个array最后位置, m+n-1是改写位置
        当然也可以加起来sort...  list.sort()是inplace sorted()是return new
    """
    s = Solution()
    print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
