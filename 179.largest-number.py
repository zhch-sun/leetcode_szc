#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#
import random

class Solution(object):
    # def largestNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: str
    #     """
    #     # 100%!
    #     strs = map(str, nums)
    #     strs.sort(cmp=lambda x, y: [-1, 1][x + y < y + x])  # 注意<时反而是1!
    #     return '0' if strs[0]=='0' else ''.join(strs)

    def insertSort(self, a, cmp):  # 38%
        # copy array实现(省略慢的swap实现): 注意第一个循环的起始条件, 第二个循环的结束条件. 
        # 注意循环过程中修改array所以不能用迭代器. 
        for i in range(1, len(a)):  # 0号位不能比较
            j, cur = i, a[i]
            while j > 0 and cmp(cur, a[j - 1]) < 0:  # 忘记 j > 0 啦; 比较的是j - 1!!
                a[j] = a[j - 1]
                j -= 1
            a[j] = cur

    def mergeSort(self, a, cmp):
        # 采用算法书的实现. 三种加速方法先不实现. 
        # recursive的实现要先判断失效指针, iterative的实现注意指针的移动!
        def merge(a, aux, lo, mid, hi): # [lo, mid], (mid, hi]
            for i in range(lo, hi + 1):
                aux[i] = a[i]
            i, j = lo, mid + 1  # Note mid + 1!!!
            for k in range(lo, hi + 1):
                if i > mid:  # 这么处理越界条件!
                    a[k] = aux[j]
                    j += 1
                elif j > hi:
                    a[k] = aux[i]
                    i += 1
                elif cmp(aux[i], aux[j]) < 0:  # Note 这里比较的aux!!!
                    a[k] = aux[i]
                    i += 1
                else:
                    a[k] = aux[j]
                    j += 1

        def sort1(a, aux, lo, hi):  #[lo, hi]
            if hi <= lo:  # 又忘记退出条件了. 
                return
            mid = lo + (hi - lo) // 2
            sort1(a, aux, lo, mid)
            sort1(a, aux, mid + 1, hi)
            merge(a, aux, lo, mid, hi)
        
        def sort2(a, aux):
            N = len(a)
            sz = 1  # 子数组大小
            while sz < N:
                for lo in range(0, N - sz, sz * 2):  # Note N - sz很重要: sz是上一次merge的最右边的区间
                    merge(a, aux, lo, lo+sz-1, min(lo+sz*2-1, N - 1)) # Note!
                sz *= 2

        aux = [None] * len(a)
        # sort1(a, aux, 0, len(a) - 1)  # 78%
        sort2(a, aux)

    def quickSort(self, a, cmp):
        def partition(a, lo, hi):  # 78%
            # Hoare Partition
            # 和书上相比, 因为python没有++i, 所以实现略有差别. 
            # 循环不变量 [lo + 1, i) [i, j] (j, hi]
            cur = a[lo]  # 最好手动缓存
            i, j = lo, hi + 1  # 不能 lo + 1, hi, 因为这样不支持part lo==hi 的情况
            while True:
                i += 1
                j -= 1   
                while i <= hi and cmp(a[i], cur) < 0:  # 不需要i < j因为右边已经排好序
                    i += 1  # i <= hi可以省略, 需要初始化时找到max并移到最右边省掉
                while j >= lo and cmp(a[j], cur) > 0:
                    j -= 1  # j >= lo 可以直接省掉
                if i >= j:  # Note >=. 前面两个循环后, 出现等于的情况只能是 a[i] == cur
                    break
                a[i], a[j] = a[j], a[i]  # 

            a[lo], a[j] = a[j], a[lo]  # 和最后一个大于lo的交换. 容易忘!
            return j  # 容易忘!

        def sort(a, lo, hi):  # [lo, hi]
            if hi <= lo:  # 至少有两个元素
                return  # 这一句可以替换成插入排序
            j = partition(a, lo, hi)
            sort(a, lo, j - 1)  # Note 这里是j-1 j+1
            sort(a, j + 1, hi)
            
        random.shuffle(a)
        sort(a, 0, len(a) - 1)

    def largestNumber(self, nums):
        # test sort functions
        strs = map(str, nums)
        # self.insertSort(strs, cmp=lambda x, y: [-1, 1][x + y < y + x])
        # self.mergeSort(strs, cmp=lambda x, y: [-1, 1][x + y < y + x])
        self.quickSort(strs, cmp=lambda x, y: [-1, 1][x + y < y + x])
        return '0' if strs[0]=='0' else ''.join(strs)
        
if __name__ == '__main__':
    """
    可以用这道题实现一下各种sort. mergesort quicksort insertsort. 
    没有公司考.. 估计是因为怎么证明呢? 
    s1 > s2 则 s2 < s1; s1 < s2, s2 < s3, 则 s1 < s3
    注意还有corner case: 多个0的输入..
    """
    s = Solution()
    print(s.largestNumber([10, 2]))
    print(s.largestNumber([3,30,34,5,9]))
    print(s.largestNumber([1,2,3,3,3,3,4,5]))
    # print(s.largestNumber([0, 0]))

