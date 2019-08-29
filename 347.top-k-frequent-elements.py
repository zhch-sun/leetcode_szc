#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#
from collections import Counter
import heapq
import itertools

class Solution(object):
    # def topKFrequent(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     count = Counter(nums)
    #     res = heapq.nlargest(k, count.items(), key=lambda x: x[1])
    #     return [item[0] for item in res]
    
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        for num, freq in Counter(nums).items():
            bucket[-freq].append(num)  # 注意freq是1-based
        return list(itertools.chain(*bucket))[:k]  # 注意输入是*bucket, 返回是iter.

if __name__ == '__main__':
    """
    1. heapq, 
    2. bucket sort: 因为被sort的东西是离散有界的, O(N), 实际不快: 
    3. quick selection做前k个数的情况还是比较复杂.
    4. 有序符号表: 复杂度是NlogN
    """
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))
    print(s.topKFrequent([1], 1))

