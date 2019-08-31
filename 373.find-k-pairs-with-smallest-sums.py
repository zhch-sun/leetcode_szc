#
# @lc app=leetcode id=373 lang=python
#
# [373] Find K Pairs with Smallest Sums
#

import heapq
import itertools

class Solution(object):
    # def kSmallestPairs(self, nums1, nums2, k):
    #     """
    #     :type nums1: List[int]
    #     :type nums2: List[int]
    #     :type k: int
    #     :rtype: List[List[int]]
    #     """
    #     g = map(lambda u: ([u+v, u, v] for v in nums2), nums1)  # 60% 外面是list, 里面是gen
    #     # g = ([[u+v, u, v] for v in nums2] for u in nums1)  # 27%
    #     g = heapq.merge(*g)  # 别忘了是 *g...
    #     return [item[1:] for item in itertools.islice(g, k)]

    def kSmallestPairs(self, nums1, nums2, k):
        def push(i, j):
            if i < M and j < N:
                heapq.heappush(hq, [nums1[i] + nums2[j], i, j])
        
        hq = []
        res = []
        M, N = len(nums1), len(nums2)
        push(0, 0)  # 应该len都大于0
        while hq and k > 0:  # 这里忘记hq了..
            _, i, j = heapq.heappop(hq)
            res.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, j)
            k -= 1
        return res

if __name__ == '__main__':
    """
    解法1:
        生成器似乎不能嵌套. 而且comprehension的写法似乎有问题? 
        最快的还是用map
    解法2:
        注意while循环中hq可能为空...
    """
    s = Solution()
    print(s.kSmallestPairs([1,7,11], [2,4,6], 3))
    print(s.kSmallestPairs([1,1,2], [1,2,3], 3))
    print(s.kSmallestPairs([1,2], [3], 3))
        

