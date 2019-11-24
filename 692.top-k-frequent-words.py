#
# @lc app=leetcode id=692 lang=python
#
# [692] Top K Frequent Words
#

from collections import defaultdict
from collections import Counter
import heapq
import random

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
        # return map(lambda x:x[0], pairs)
        # return list(zip(*pairs))[0]
        return [x[0] for x in pairs]

    # def topKFrequent(self, words, k):
    #     def partition(a, lo, hi):
    #         cur = a[lo]
    #         i, j = lo, hi + 1
    #         while True:
    #             i += 1
    #             j -= 1
    #             while i <= hi and a[i] < cur:
    #                 i += 1
    #             while j >= lo and a[j] > cur:
    #                 j -= 1
    #             if i >= j:
    #                 break
    #             a[i], a[j] = a[j], a[i]
    #         a[lo], a[j] = a[j], a[lo]
    #         return j

    #     def sort(a, lo, hi):
    #         if lo >= hi:
    #             return
    #         j = partition(a, lo, hi)
    #         sort(a, lo, j - 1)
    #         if j + 1 < K:
    #             sort(a, j + 1, hi)
        
    #     pairs = list(Counter(words).items())
    #     pairs = [(~x[1], x[0]) for x in pairs]  # 前处理后不需要cmp函数
    #     random.shuffle(pairs)
    #     K = k
    #     sort(pairs, 0, len(pairs) - 1)
    #     return [x[1] for x in pairs[:K]]

if __name__ == '__main__':
    """
    题设: 统计一堆word出现的次数, 返回前k个高频单词, 如果个数相同, 按照a < aa排序. 
    解法1: 
        重要的是str的顺序和int的顺序是相反的, 
        d后面必须跟着 .items()
        通过 非~把int反序 比 *-1 快得多
        Counter可以通过defaultdict来实现
        复杂度: NlogK
    解法2:
        quick select实现: 就是在sort第二个递归加一条判断
        复杂度计算: KlogK + log(N-K) ? 
        实际要慢一点. 
    解法3:
        前缀树. 字符串的排序要想到前缀树! 
    其他解法: 
        2 quick selection复杂不写
        3 bucket sort: 不行, 还有个str的排序...
        4 红黑树不行: 复杂度也是NlogN
    """
    s = Solution()
    print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    print(s.topKFrequent(['aaa', 'aa', 'a'], 1))


