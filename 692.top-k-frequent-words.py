#
# @lc app=leetcode id=692 lang=python
#
# [692] Top K Frequent Words
#

from collections import defaultdict
from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # d = defaultdict(int)
        # for i in words:
        #     d[i] += 1
        d = Counter(words)
        items = list(d.items())
        pairs = heapq.nsmallest(k, items, key=lambda x: (~x[1], x[0]))  # Note 多个条件sort时的比较.
        # return list(zip(*pairs))[0][:k]
        return [i[0] for i in pairs][:k]

if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    print(s.topKFrequent(['aaa', 'aa', 'a'], 1))


