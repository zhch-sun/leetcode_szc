#
# @lc app=leetcode id=668 lang=python
#
# [668] Kth Smallest Number in Multiplication Table
#

import itertools
import heapq

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # def count(mid, m, n):
        #     j = n - 1
        #     count = 0
        #     for i in xrange(0, m):
        #         while j < n and (i + 1) * (j + 1) > mid:
        #             j -= 1
        #         count += j + 1
        #     return count
        
        def count(mid, m, n):
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(mid // i, n)  # 注意这里的min函数
            return cnt

        lo, hi = 1, m * n  # (m, n)
        while lo < hi:  # [lo, hi]
            mid = lo + (hi - lo) // 2
            cnt = count(mid, m, n)
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # def findKthNumber(self, m, n, k):
    #     # MLE, 内环必须list, 但仍然MLE
    #     matrix = ([i * j for i in xrange(1, m + 1)] for j in xrange(1, n + 1))  
    #     hq = heapq.merge(*matrix)
    #     return list(itertools.islice(hq, k))[-1]
        
if __name__ == '__main__':
    """
    pq方法, 不能generator 套 generator, 内环需要是list. 但是直接生成还是会MLE
    二分查找可以通过除法count..., 而且要注意那个min函数...
    """
    s = Solution()
    print(s.findKthNumber(3,3,5))
    print(s.findKthNumber(2,3,6))
