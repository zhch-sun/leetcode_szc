#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """参考答案解法1 o(log(min(m, n))). 更通用但更慢. 
        假设中位数是第k个. 
        数列删除法. 两个数列比较2/k的位置, 
        如果A<B则意味着A一定比第K个小, 删除A前面所有数, 
        然后剩下2/K个数, 比较两个数列的各自的前4/k. 
        """
    def findMedianSortedArrays(self, nums1, nums2):
        """参考答案解法2 o(log(m + n))"""
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        lo, hi = 0, m   # [lo, hi] 取到m的时候意味着中位数a里, 包括m==0的情况; 取0的时候不在a里
        half = (m + n + 1) // 2  # 偶数的时候可能出现在左右, 奇数的时候只在左边
        while lo <= hi:  # 一定进入循环
            i = lo + (hi - lo) // 2  # i和j代表个数
            j = half - i  # [0, i-1], [i, m-1]; [0, j-1] [j, n-1]
            if i > 0 and a[i - 1] > b[j]:  # 因为i-1所以i>0; m=n=0或者m=0 n=1的时候, j能取到n
                hi = i - 1
            elif i < m and a[i] < b[j - 1]: # i==m时j才能取到0, 包括m=n=0的情况
                lo = i + 1
            else:  # i是正确的
                if i == 0:
                    maxL = b[j - 1]
                elif j == 0:
                    maxL = a[i - 1]
                else:
                    maxL = max(a[i - 1], b[j - 1])
                if (m + n) % 2 == 1:
                    return maxL
                
                if i == m:  # 右边是min!!!
                    minR = b[j]
                elif j == n:
                    minR = a[i]
                else:
                    minR = min(a[i], b[j])
                return (maxL + minR) / 2.0

    # def findMedianSortedArrays(self, nums1, nums2):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :rtype: float
    #     """
    #     # 最简单的解法, 但是没有理解
    #     a, b = sorted((nums1, nums2), key=len)
    #     m, n = len(a), len(b)
    #     after = (m + n - 1) // 2  # 奇数时是中位数的index, 偶数时左半边最后的index
    #     lo, hi = 0, m  # i是a[:i]的取值范围, j则是b[:j]的取值范围
    #     while lo < hi:  # [lo, hi]
    #         i = lo + (hi - lo) // 2
    #         j = after - i  # non-inclusive所以m+n-1
    #         # i取不到m, 那时lo==hi, 在前面循环跳出.
    #         # i=0时, j最大值(m+n-1)//2; i=n-1时, j最小值
    #         if j < 1 or a[i] >= b[j - 1]:  #没有数了自然是无限小? 等于号!
    #             hi = i
    #         else:  # 两种情况, 如果b[j-1] <= a[i-1]则正确, 如果b[j-1] > a[i-1]需要增大
    #             lo = i + 1
        
    #     i = lo  # i可能未定义
    #     j = after - i  # 不是 -i, i可能未定义
    #     center = sorted(a[i:i+2] + b[j:j+2])  # len可能是1, 2, 3, 4...
    #     return (center[0] + center[1 - (m+n)%2]) / 2.0


if __name__ == '__main__':
    """    
    理解答案解法一, 实际使用答案解法二. 
        在a上二分，由a的位置i可以直接确定b的位置j。a一定要是更短的那个数组. 
        如果a[i-1]<b[j]且b[j-1]<a[i], 则中位数一定出现在边界上. 即maxL和minR是中位数.
        [0, i-1], [i, m-1]
        [0, j-1], [j, n-1]
        访问数组时需要考虑i和j的取值范围, 只需要判断i! j可以自动推导出来. 

    并没有理解最简单的解法. 
        奇数的时候, i或者j是中位数index, 偶数的时候两个的均值是index.
        之所以两边都要+2, 左边: [1,2] [-1,3], 右边[], [2,3]
        核心思路是在短的数组上二分(根据中位数的性质自动求出长数组上的位置), 
            而a[i]>b[j-1], a[j]>a[i-1]是正确条件
        最简单的处理是a[:i] + b[:j]是non-inclusive的左半边, 求i. 
            采取non-inclusive的原因是, 包含情况越少, 处理越简单. i>=j-1, j>=i-1
            这时候的i是第一个>=j-1的值!
            因为i>j-1时i-1<=j-2<=j, 即满足条件. 所以只考虑i即可.
        结尾处理:
            通常情况下要么是a[i], 要么是b[j]
            之所以两边都要+2, 左边: [1,2] [-1,3], 右边[], [2,3]
    """
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]))
    print(s.findMedianSortedArrays([1,2], [3,4]))
    print(s.findMedianSortedArrays([1,2], [-1,3]))
    # print(s.findMedianSortedArrays([1,3], [2,4]))
    # print(s.findMedianSortedArrays([], [1]))
    # print(s.findMedianSortedArrays([], [2,3]))
    # print(s.findMedianSortedArrays([3], [1,2,4]))
    # print(s.findMedianSortedArrays([1,2,3], [4,5,6]))
