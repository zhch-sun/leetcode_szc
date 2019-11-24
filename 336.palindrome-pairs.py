#
# @lc app=leetcode id=336 lang=python
#
# [336] Palindrome Pairs
#

# @lc code=start
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isEnd = False

class Trie(object):  # 不写trie写法了...
    def __init__(self):
        self.root = TrieNode()
    def put(self, word):
        cur = self.root
        for char in word:
            cur = cur.nodes[char]
        cur.isEnd = True

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPal(w, i, j):  # [i, j)
            j -= 1
            while i < j:
                if w[i] != w[j]:
                    return False
                i += 1
                j -= 1
            return True

        d = {}
        ans = set()  # 需要除重..
        for i, w in enumerate(words):
            d[w[::-1]] = i  # Note 不能用reversed...
        for i, w in enumerate(words):
            N = len(w)
            for j in xrange(N + 1):
                if isPal(w, 0, j):  # 如果前面是回文, 检查suffix是否有对称
                    suffix = w[j:]
                    if suffix in d and d[suffix] != i:
                        ans.add((d[suffix], i))
                if isPal(w, j, N):
                    prefix = w[:j]
                    if prefix in d and d[prefix] != i:
                        ans.add((i, d[prefix]))
        return list(ans)

if __name__ == '__main__':
    """
    题设: 
        必须是两个word构成. 
    解法1: Trie
        https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n-*-k2)-java-solution-with-Trie-structure
        仍然很麻烦. 需要处理两种情况
            trie结束了, 扫描word剩下的部分
            word结束了, 扫描trie剩下的部分
        不写了.
    解法2:
        1. 每一个word和index放到dict中
        2. 每一个word分成str1和str2, 
            如果word在左边, 则当str2回文时, 找str1的对偶
            如果word在右边, 则当str1回文时, 找str2的对偶
    """
    s = Solution()
    print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))
        
# @lc code=end

