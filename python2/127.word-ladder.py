#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#
from collections import deque, defaultdict

class Solution(object):
    # def ladderLength(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: int
    #     """    
    #     wordSet = set(wordList)
    #     if not wordSet:
    #         return 0
    #     alpha = 'abcdefghijklmnopqrstuvwxyz'
    #     bucket = defaultdict(set)  # key虚拟, value是word
    #     for w in wordSet:
    #         for i in xrange(len(w)):
    #             for c in alpha:
    #                 # if c != w[i]:  # 可以省掉
    #                 bucket[w[:i] + c + w[i + 1:]].add(w)
    #     dq = deque([(beginWord, 1)])  # note 又忘记[]了..
    #     memo = {beginWord}  # 需要memo除重.
    #     while dq:
    #         cur, step = dq.popleft()
    #         if cur == endWord:
    #             return step
    #         for item in bucket[cur]:
    #             if item not in memo:
    #                 dq.append((item, step + 1))
    #                 memo.add(item)
    #     return 0

    # def ladderLength(self, beginWord, endWord, wordList):
    #     wordSet = set(wordList)
    #     if not wordSet:
    #         return 0
    #     alpha = 'abcdefghijklmnopqrstuvwxyz'
    #     dq = deque([(beginWord, 1)])  # note 又忘记[]了..
    #     memo = {beginWord}  # 需要memo除重.
    #     while dq:
    #         cur, step = dq.popleft()
    #         if cur == endWord:
    #             return step
    #         for i in xrange(len(cur)):
    #             before, after = cur[:i], cur[i + 1:]
    #             for c in alpha:
    #                 item = before + c + after
    #                 if item in wordSet and item not in memo:
    #                     dq.append((item, step + 1))
    #                     memo.add(item)
    #     return 0

    # def ladderLength(self, beginWord, endWord, wordList):
    #     wordSet = set(wordList)
    #     if not wordSet or endWord not in wordSet:
    #         return 0
    #     alpha = 'abcdefghijklmnopqrstuvwxyz'
    #     frontSet = set([beginWord])  # Note[]...
    #     endSet = set([endWord])  # Note[]...
    #     wordSet.remove(endWord)
    #     step = 1
    #     while frontSet:  # 不是front and end!!!
    #         tmp = set()  # 直接初始化为set
    #         for cur in frontSet:
    #             for i in xrange(len(cur)):
    #                 before, after = cur[:i], cur[i + 1:]
    #                 for c in alpha:
    #                     item = before + c + after
    #                     if item in endSet:
    #                         return step + 1
    #                     if item in wordSet:
    #                         tmp.add(item)
    #                         wordSet.remove(item)
    #         frontSet = tmp
    #         if len(frontSet) > len(endSet):
    #             frontSet, endSet = endSet, frontSet            
    #         step += 1
    #     return 0

    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if not wordSet or endWord not in wordSet:
            return 0
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        frontSet = set([beginWord])  # Note[]...
        endSet = set([endWord])  # Note[]...
        wordSet.remove(endWord)
        step = 1
        while frontSet:  # 不是front and end!!!
            tmp = set()  # 直接初始化为set
            for cur in frontSet:
                for i in xrange(len(cur)):
                    before, after = cur[:i], cur[i + 1:]
                    for c in alpha:
                        tmp.add(before + c + after)
            frontSet = tmp
            if frontSet & endSet:
                return step + 1
            frontSet &= wordSet
            wordSet -= frontSet
            if len(frontSet) > len(endSet):
                frontSet, endSet = endSet, frontSet            
            step += 1
        return 0

if __name__ == '__main__':
    """
    题设: 
        词语梯子. 所有的单词长度相同. 无重复. 都是小写字母. 
        begin在dict里, end不在
        每次只允许变一个字符, 求首尾之间的最短路径长. 
        126题返回最短路径. 
        分析同839题. 
    解法1:
        最短路显然bfs, 两种做法的复杂度分析: 
            建立完整的图(邻接矩阵表示). 复杂度 N*N*W
            对每个word穷举可能性, 找字典中是否存在, O(N*W*W*26)
            所以 N > W 时, 选第二种情况.
        所以生成了一个二分图, 
            key是所有可能的变化, value是字典中实际存在的值.
    解法2:
        不是所有的结点都会访问到. 所以在BFS图中建图
    解法3:
        从头尾搞, 三个互斥的set: front end word.
        也不需要memo除重. 
    解法4: 
        上一个解法用set向量化操作, 并不快. 
    解法5：
        预先处理wordList，用 _ 代替当前位置，不快不搞
    """
    s = Solution()
    print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]))
