#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#
from collections import deque

class Solution(object):
    # def ladderLength(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: int
    #     """
    #     words = set(wordList)
    #     if endWord not in words:
    #         return 0
    #     visited = deque([(beginWord, 1)])
    #     alpha = 'abcdefghijklmnopqrstuvwxyz'

    #     while visited:
    #         word, num_transform = visited.popleft()
    #         for idx in range(len(word)):
    #             for char in alpha:
    #                 # if char != word[idx]:  # 可以省去这个逻辑. 
    #                 tmp = word[:idx] + char + word[idx + 1:]
    #                 if tmp == endWord:
    #                     return num_transform + 1  # 第一个找到的一定是最短的
    #                 if tmp in words:
    #                     visited.append((tmp, num_transform + 1))
    #                     words.remove(tmp)  # 不remove是错的
    #     return 0

    # def ladderLength(self, beginWord, endWord, wordList):
    #     words = set(wordList)
    #     if endWord not in words:
    #         return 0
    #     visited = deque([(beginWord, 1)])
    #     alpha = 'abcdefghijklmnopqrstuvwxyz'

    #     while visited:
    #         curWord, steps = visited.popleft()
    #         if curWord == endWord:
    #             return steps
    #         for i in range(len(curWord)):
    #             for char in alpha:
    #                 tmp = curWord[:i] + char + curWord[i+1:]
    #                 if tmp in words:
    #                     visited.append((tmp, steps + 1))
    #                     words.remove(tmp)
    #     return 0
    

    def ladderLength(self, beginWord, endWord, wordDict):
        words = set(wordDict)
        if endWord not in words:
            return 0
        visited = deque([(beginWord, 1)])
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        while visited:
            curWord, steps = visited.popleft()
            if curWord == endWord:
                return steps
            for i in range(len(curWord)):
                for char in alpha:
                    tmp = curWord[:i] + char + curWord[i+1:]
                    if tmp in words:
                        visited.append((tmp, steps + 1))
                        words.remove(tmp)
        return 0

    # def ladderLength(self, beginWord, endWord, wordDict):
    #     wordDict = set(wordDict)
    #     if endWord not in wordDict:
    #         return 0
    #     length = 2
    #     front, back = set([beginWord]), set([endWord])
    #     wordDict.discard(beginWord)  # 相比remove的区别是如果没有key, do nothing
    #     while front:
    #         # generate all valid transformations
    #         front = wordDict & (set(word[:index] + ch + word[index+1:] \
    #                             for word in front \
    #                             for index in range(len(beginWord)) \
    #                             for ch in 'abcdefghijklmnopqrstuvwxyz'))
    #         if front & back:
    #             # there are common elements in front and back, done
    #             return length
    #         length += 1
    #         if len(front) > len(back):
    #             # swap front and back for better performance (fewer choices in generating nextSet)
    #             front, back = back, front  # 这个要求初始的时候endWord必须在wordDict里. 
    #         # remove transformations from wordDict to avoid cycle
    #         wordDict -= front
    #     return 0

if __name__ == '__main__':
    """
    词语梯子.  所有的word length相同.  没有duplicates. 都是小写26个字母. 
    这个题返回长度, 还有个更难的126返回所有sequence. 这题目有很多优化空间. 
    
    是一个无向图, bfs搜索.
    确实要注意重复情况, 一个词语的25*L条边没有重复, 但是变两次之后就会重复, 所以有
    两个解决方案: 1.搞一个visited set, 存储之前访问过的节点. 2. 每次访问一个就从dict里面删掉. 

    解法1: python里的string是不可修改的, 所以我这里只能重新生成新string 
        beginWord[:idx] + char + beginWord[idx + 1:]. 这样速度太慢了. 
    解法2: 解法1的逻辑不够好. 对于这种题, 每次pop后应该紧跟return条件, 而不是在后面的循环中
        去check条件. 解法1给出正确答案有运气成分.. 前两种解法的好处是空间复杂度很小, 但是for循环很慢. 
    解法3: 两个修改, 1. 内部对alpha的循环改成set操作. 2. 从前后两边forward. 不用queue了. 
    """
    s = Solution()
    print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]))
