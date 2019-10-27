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
    #     def insertSort(a, lo=None, hi=None):  # [lo, hi]
    #         # copy array实现(省略慢的swap实现)
    #         lo = 0 if lo is None else lo
    #         hi = len(a) - 1 if hi is None else hi
    #         for i in xrange(lo, hi + 1):  # Note hi + 1
    #             cur, j = a[i], i
    #             while j > 0 and a[j - 1] > cur: # > 确保stable
    #                 a[j] = a[j - 1]  # Note 赋值方向
    #                 j -= 1  # Note 1.忘记这里 2.写成+=
    #             a[j] = cur  # Note 忘记
        
    #     def mergeSort(a):
    #         def merge(a, aux, lo, mid, hi):
    #             i, j = lo, mid + 1 # 双指针移动
    #             for k in range(lo, hi + 1):
    #                 aux[k] = a[k]
    #             for k in range(lo, hi + 1):
    #                 if i > mid:  # 左边结束了
    #                     a[k] = aux[j]
    #                     j += 1
    #                 elif j > hi:  # 右边结束了
    #                     a[k] = aux[i]
    #                     i += 1  
    #                 # 为了stable等于号是必须的
    #                 # 算法书只定义小于号less(), 所以是less(aux[j], aux[i])
    #                 elif aux[i] <= aux[j]:  # Note这里是aux不是a!
    #                     a[k] = aux[i]
    #                     i += 1
    #                 else:
    #                     a[k] = aux[j]
    #                     j += 1
            
    #         def sort1(a, aux, lo, hi):
    #             if lo >= hi:  # 没有+1!!
    #                 return  # 这里如果加入insert, 会TLE, 但是代码应该没问题.
    #             mid = lo + (hi - lo) // 2
    #             sort1(a, aux, lo, mid)
    #             sort1(a, aux, mid + 1, hi)  # Note wfpmid+1
    #             merge(a, aux, lo, mid, hi)  # Note 忘记写了..
            
    #         def sort2(a, aux):
    #             sz = 1  # sz是一边的大小
    #             N = len(a)
    #             while sz < N:
    #                 # N - sz是因为上一个sz已经被排好序了!
    #                 for i in xrange(0, N - sz, sz * 2):
    #                     # 通过[0,1]两个位置确定需要-1, 以及处理循环最后的情况
    #                     # 前面的N-sz确定i+sz-1不用min
    #                     merge(a, aux, i, i+sz-1, min(N-1, i+sz*2-1)) # Note不是N
    #                 sz *= 2
                    
    #         aux = [None] * len(a)
    #         # sort1(a, aux, 0, len(a) - 1)
    #         sort2(a, aux)
        
        def quickSort(a):
            # Hoare Partition
            # 循环不变量 (lo, i) [i, j] (j, hi+1)
            def partition(a, lo, hi):
                cur = a[lo]
                i, j = lo, hi + 1  # lo是取不到的, 和hi+1一样
                while True:
                    i += 1
                    j -= 1
                    # 这里i<=hi也可以写成i<=j, 但实际和j>=lo都可以省掉: 先写成i<=hi吧
                    # 注意a[j]和cur的> <容易反啊.. 而且不加=, 即遇到=的情况也停下
                    while i <= hi and a[i] < cur:
                        i += 1
                    while j >= lo and a[j] > cur:  
                        j -= 1
                    if i >= j:  # =的时候是同一个数, 自然可以停下.
                        break  # 结束的时候a[i] >= cur, a[j] <= cur, 所以换j
                    a[i], a[j] = a[j], a[i]
                a[lo], a[j] = a[j], a[lo]  # 记住partition返回的是j, 即和j交换
                return j

            def sort(a, lo, hi):
                # [lo, hi]
                if lo >= hi:  # 78%
                    return  # 递归先写return条件!
                # if lo + 8 >= hi:
                #     insertSort(a, lo, hi)  # 78 %
                #     return
                j = partition(a, lo, hi)
                sort(a, lo, j - 1)
                sort(a, j + 1, hi)

            random.shuffle(a)            
            # maxValue = max(a)
            # maxPos = a.index(maxValue)
            # a[maxPos], a[-1] = a[-1], a[maxPos]
            sort(a, 0, len(a) - 1)

        def quick3way(a):
            def partition3(a, lo, hi):
                # 3way partition
                # [lo, i), [i, k), [k, j], (j, hi]
                cur = a[lo]
                i, k, j = lo, lo, hi
                while k <= j:
                    if a[k] < cur:
                        a[i], a[k] = a[k], a[i]
                        i += 1
                        k += 1
                    elif a[k] == cur:
                        k += 1
                    else:
                        a[k], a[j] = a[j], a[k]
                        j -= 1
                return i, j  # 返回两个值!

            def sort(a, lo, hi):
                if lo >= hi:
                    return
                i, j = partition3(a, lo, hi)
                sort(a, lo, i - 1)
                sort(a, j + 1, hi)

            random.shuffle(a)
            sort(a, 0, len(a) - 1)

        # # nums.sort()  # 99%
        # insertSort(nums, 0, len(nums) - 1)  # TLE
        # # mergeSort(nums)  # 40%
        # quickSort(nums)  # 78%
        quick3way(nums)
        return nums


if __name__ == '__main__':
    """
    题设: 要求return nums
    有关hi+1, 算法数就是这么定义的.先这样做吧. 
    TODO 理解mergesort2的各种条件...
    """
    s = Solution()
    print(s.sortArray([5,2,3,1]))
    print(s.sortArray([5,1,1,2,0,0]))
