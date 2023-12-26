#
# @lc app=leetcode id=378 lang=python
#
# [378] Kth Smallest Element in a Sorted Matrix
#
import itertools
import heapq
class Solution(object):
    # def kthSmallest(self, matrix, k):
    #     """
    #     :type matrix: List[List[int]]
    #     :type k: int
    #     :rtype: int
    #     """
    #     # Nlog(max-min), 140ms 97%
    #     M, N = len(matrix), len(matrix[0])
    #     lo, hi = matrix[0][0], matrix[-1][-1]
        
    #     while lo < hi:  # k in [lo, hi]
    #         mid = lo + (hi - lo) // 2  # integer num
    #         cnt = 0
    #         j = N - 1  # 在下面的for循环中, j只会变小
    #         for i in xrange(0, M):  # 直接写会写出while. for循环需要背过
    #             while j >= 0 and matrix[i][j] > mid:
    #                 j -= 1
    #             cnt += (j + 1)
    #         if cnt < k:
    #             lo = mid + 1
    #         else:
    #             hi = mid
    #     return lo

    # def kthSmallest(self, matrix, k):
    #     # # bruteforce heapq n**2 logK  216ms 56%
    #     # return heapq.nsmallest(k, list(itertools.chain(*matrix)))[-1]

    #     # # heap merge max(n,k)logN  216ms 56%
    #     hq = heapq.merge(*matrix)
    #     # return list(itertools.islice(hq, k))[-1]

    def kthSmallest(self, matrix, k):        
        # 下面是手动实现heap的merge算法
        def push(i, j):
            if i < M and j < N:
                heapq.heappush(pq, (matrix[i][j], i , j))
        M, N = len(matrix), len(matrix[0])  # 224ms
        pq = []
        push(0, 0)
        while k > 0:
            num, i, j = heapq.heappop(pq)
            push(i, j + 1)
            if j == 0:  # Note 忘记M-1了!
                push(i + 1, j)
            k -= 1
        return num

if __name__ == '__main__':
    """
    二分查找写法 Nlog(max-min):
        该方法只支持整数元素, 浮点数可以在count内部记录最大值
        普通的二分查找lo hi是index, 因为ind和数目是正比的. 这个题目lo hi是num, 因为不完全sorted.
        解一定存在, 且在[lo, hi]之间, 所以可以用return lo的写法... 一开始居然没有想到
            不能count==k的时候return mid. 因为count是<=mid的个数, 等于号不一定能取到
        count的2-pointers方法很精妙
            找到一个mid值之后, count一下小于mid值的个数, 注意j的复用方式...
        题目保证matrix和k valid, 且是方阵. 为了general我就写M, N了
        
    pq标准库写法 max(n,k)logN: 
        chain和heap merge写法. merge的写法更好. 
        merge的输入是若干排序好的list. 
        实现方式先把所有iter放进去, 就是pop哪个, 就push哪个iter后面的进去. 返回一个generator.
        generator需要用islice拿到第k个.
        
    pq手动实现: 仍然可能用到.. 373只能这么搞
        从左上角开始, 每次pop之后, 把比它大的加到pq中. 
        因为除重, 这时我们可以pop之后只加入右边的, 只有j==0时才加入下边的. 
        需要注意i, j范围, 也可以把push包装成函数, 里面判断 j < N -1; i < M - 1
        
        归纳法证明: 未来最小值一定在当前堆+当前最小值的直接可达区域内.  
        问题是要除重, 一个元素既可以被左边的元素加入, 又可以被上面的元素加入.
        所以只加一边就可以, 比如加右边, 下面的元素让下面一行加入即可. 
        这样只j=0时加入下面就可以.

        和dijkstra相似? 但是图的角度没法理解. 
    
    O(n)论文: 不管了.
    """
    s = Solution()
    matrix = [
        [1,   5,  9],
        [10, 11, 13],
        [12, 13, 15],
    ]
    print(s.kthSmallest(matrix, 8))

