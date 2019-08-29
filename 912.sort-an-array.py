#
# @lc app=leetcode id=912 lang=python
#
# [912] Sort an Array
#
import random
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def insertSort(a, lo, hi):
            for i in range(lo, hi + 1):
                cur, j = a[i], i
                while j > 0 and cur < a[j - 1]:
                    a[j] = a[j - 1]
                    j -= 1
                a[j] = cur
        
        def mergeSort(a):
            def merge(a, aux, lo, mid, hi):
                i, j = lo, mid + 1
                for k in range(lo, hi + 1):
                    aux[k] = a[k]
                for k in range(lo, hi + 1):
                    if i > mid:
                        a[k] = aux[j]
                        j += 1
                    elif j > hi:
                        a[k] = aux[i]
                        i += 1
                    elif aux[i] < aux[j]:
                        a[k] = aux[i]
                        i += 1
                    else:
                        a[k] = aux[j]
                        j += 1
            
            def sort1(a, aux, lo, hi):
                if lo >= hi:
                    return
                mid = lo + (hi - lo) // 2
                sort1(a, aux, lo, mid)
                sort1(a, aux, mid + 1, hi)
                merge(a, aux, lo, mid, hi)
            
            def sort2(a, aux):
                sz = 1  # sz是一边的大小
                N = len(a)
                while sz < N:
                    for i in range(0, N - sz, sz * 2):
                        merge(a, aux, i, i + sz - 1, min(N-1, i + sz * 2 - 1))
                    sz *= 2
                    
            aux = [None] * len(a)
            # sort1(a, aux, 0, len(a) - 1)
            sort2(a, aux)
        
        def quickSort(a):
            def partition(a, lo, hi):
                cur = a[lo]
                i, j = lo, hi + 1
                while True:
                    i += 1
                    j -= 1
                    while i <= hi and a[i] < cur:
                        i += 1
                    while j >= lo and a[j] > cur:
                        j -= 1
                    if i >= j:
                        break
                    a[i], a[j] = a[j], a[i]
                a[lo], a[j] = a[j], a[lo]
                return j

            def sort(a, lo, hi):
                # [lo, hi]
                # if lo >= hi:  # 70
                #     return
                if lo + 16 >= hi:
                    insertSort(a, lo, hi)  # 78 %
                    return
                j = partition(a, lo, hi)
                sort(a, lo, j - 1)
                sort(a, j + 1, hi)
            random.shuffle(a)
            sort(a, 0, len(a) - 1)

        # nums.sort()  # 95%
        # insertSort(nums, 0, len(nums) - 1)  # TLE
        # mergeSort(nums)  # 40%
        quickSort(nums)  # 70% or 78%
        return nums
        
if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.sortArray([5,2,3,1]))
    print(s.sortArray([5,1,1,2,0,0]))
