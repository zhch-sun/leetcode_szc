#
# @lc app=leetcode id=336 lang=python
#
# [336] Palindrome Pairs
#

# @lc code=start
from collections import defaultdict

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
        for i, w in enumerate(words):  # 必须初始化
            d[w[::-1]] = i  # Note 不能用reversed...
        for i, w in enumerate(words):
            N = len(w)
            for j in xrange(N + 1):  # Note N + 1
                if isPal(w, 0, j):  # 如果前面是回文, 检查suffix是否有对称
                    suffix = w[j:]
                    if suffix in d and d[suffix] != i:
                        ans.add((d[suffix], i))
                if isPal(w, j, N):
                    prefix = w[:j]  # 这里要求上门N+1
                    if prefix in d and d[prefix] != i:
                        ans.add((i, d[prefix]))
        return list(ans)

if __name__ == '__main__':
    """
    题设: 
        有个字典里有words. 两个word加一起是回文.
        找到所有这种组合. 
    解法1:
        1. 每一个word和index放到dict中
        2. 每一个word分成str1和str2, 
            如果word在左边, 则当str2回文时, 找str1的对偶
            如果word在右边, 则当str1回文时, 找str2的对偶   
        TODO: 用[::-1]判断回文应该更快?     
    解法2: 
        Trie
        https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n-*-k2)-java-solution-with-Trie-structure
        仍然很麻烦. 需要处理两种情况
            trie结束了, 扫描word剩下的部分
            word结束了, 扫描trie剩下的部分
        不写了.
    """
    s = Solution()
    print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))
        
# @lc code=end

