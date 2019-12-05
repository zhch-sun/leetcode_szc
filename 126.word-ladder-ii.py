#
# @lc app=leetcode id=126 lang=python
#
# [126] Word Ladder II
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        if not wordSet or endWord not in wordSet:
            return []
        # wordSet.remove(endWord)  # 不能.
        front = set([beginWord])
        parent = defaultdict(set)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        while front:
            tmp = set()
            for item in front:
                for i in xrange(len(item)):
                    before, after = item[:i], item[i+1:]
                    for c in alpha:
                        candi = before + c + after
                        if candi in wordSet:
                            # wordSet.remove(endWord)
                            tmp.add(candi) # 不remove
                            parent[candi].add(item)  # add!
            front = tmp
            if endWord in front:
                ans = [[endWord]]
                while ans[0][0] != beginWord:
                    ans = [[item] + path for path in ans \
                        for item in parent[path[0]]]
                return ans             
            wordSet -= front
        return []

if __name__ == '__main__':
    """
    题设: 返回所有最短路径
    解法1:
        bfs中存储所有路径, 但是空间复杂度太高. 
        未写
    解法2:
        用一个 dict[set] 存储parent.
            不同的node可能有一个相同的parent.
            同一个node可以有几个parent:
                关键是此时所有parent长度相同!
                因为是在同一次循环赋值的.
                循环结束child就被删掉了
        最后输出路径:
            直接正序反而速度最快.
            反序还要最后[::-1]
            就是[item] + path..
            因为反正每次都要copy..
    解法3:
        解法2基础上还可以front end..
    """
    s = Solution()
    print(s.findLadders("hit", 'cog', ["hot","dot","dog","lot","log","cog"]))
    print(s.findLadders("hit", 'cog', ["hot","dot","dog","lot","log"]))
# @lc code=end

