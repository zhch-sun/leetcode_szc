#
# @lc app=leetcode id=212 lang=python
#
# [212] Word Search II
#

from collections import defaultdict


class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.val = None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def put(self, word):
        cur = self.root
        for char in word:
            cur = cur.nodes[char]
        cur.val = word

    # def get(self, word):  # 其实不需要
    #     cur = self.root
    #     for char in word:
    #         cur = cur.nodes.get(char, None)
    #         if cur is None:
    #             return False
    #     return True if cur.isEnd else False

    def prefix(self, char, root):
        return root.nodes.get(char, None)

class Solution(object):        
    def findWords(self, board, words):
        def dfs(i, j, root):
            dirs = ((1,0), (0,1), (-1,0), (0,-1))
            root = trie.prefix(board[i][j], root)
            if not root:  # 没有前缀
                return
            if root.val:
                ans.append(root.val)
                root.val = None
            tmp, board[i][j] = board[i][j], '#'
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < M and 0 <= nj < N:
                    dfs(ni, nj, root)
            board[i][j] = tmp
            return
        if not board or not board[0]:
            return False
        M, N = len(board), len(board[0])
        trie = Trie()
        for w in words:
            trie.put(w)
        ans = []
        for i in xrange(M):
            for j in xrange(N):
                dfs(i, j, trie.root)
        return ans

if __name__ == '__main__':
    """
    题设: 
        二维棋盘上搜索若干字符串, 一个字符不允许被一个单词重复使用.
        79th只搜索一个词. 
    解法1:
        trie数针对words生成一个字典. 
        需要加速: 找prefix时提供当前的node. 因为直接用trie每次都要完整的前缀.
        除重: 
            大规模应用时, 更好的解法应该是删掉node和上面所有空分支. 
            这个解法直接删node里的val. 
    解法2:
        用set()除重...
    """
    board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
    ]    
    words = ["oath","pea","eat","rain"]
    s = Solution()
    print(s.findWords(board, words))

    # board = [
    # ['a', 'b'],
    # ['a', 'a'],
    # ]
    # words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
    # s = Solution()
    # print(s.findWords(board, words))
