#
# @lc app=leetcode id=212 lang=python
#
# [212] Word Search II
#

from collections import defaultdict

# class TrieNode(object):
#     def __init__(self):
#         self.nodes = defaultdict(TrieNode)
#         self.isEnd = False

# class Trie(object):
#     def __init__(self):
#         self.root = TrieNode()
#         self.root.isEnd = True
    
#     def insert(self, word):
#         cur = self.root
#         for char in word:
#             cur = cur.nodes[char]
#         cur.isEnd = True

#     def hasPrefix(self, word, cur=None):  # 稍微修改接口, 但通用
#         cur = self.root if cur is None else cur
#         for char in word:
#             cur = cur.nodes.get(char)
#             if cur is None:
#                 return False
#         return cur  # 不能返回一个string flag.. 因为未来还要用这个node继续寻找..


# class Solution(object):
    # def findWords(self, board, words):
    #     """
    #     :type board: List[List[str]]
    #     :type words: List[str]
    #     :rtype: List[str]
    #     """
    #     def dfs(i, j, path, node, res, word):
    #         # i, j is the cur pos, path contains (i, j)
    #         word += board[i][j]
    #         node = trie.hasPrefix(board[i][j], node)
    #         if node == False:
    #             return
    #         if node.isEnd:  # 直接调用这个接口..
    #             # 这里错了... set是无序的..
    #             # return res.add(''.join([board[i][j] for i, j in path]))
    #             # return res.add(word)  # 这里又错了.. 不能return... 还需要继续搜索..
    #             res.add(word)
    #         choices = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    #         for ni, nj in choices:
    #             if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in path:
    #                 path.add((ni, nj))
    #                 dfs(ni, nj, path, node, res, word)
    #                 path.remove((ni, nj))

    #     # build trie
    #     trie = Trie()
    #     for w in words:
    #         trie.insert(w)
    #     # search the board
    #     res = set([])
    #     m = len(board)  # num of rows
    #     n = len(board[0])
    #     for i in range(m):
    #         for j in range(n):
    #             dfs(i, j, set([(i, j)]), trie.root, res, '')
    #     return list(res)

class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.word = None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for char in word:
            cur = cur.nodes[char]
        cur.word = word

class Solution(object):        
    def findWords(self, board, words):
        def dfs(i, j, res, node):
            node = node.nodes.get(board[i][j])
            if node is None:
                return
            if node.word is not None:
                res.append(node.word)
                node.word = None
            save, board[i][j] = board[i][j], None
            for ni, nj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] is not None:  # 写成了board[i][j]
                    dfs(ni, nj, res, node)
            board[i][j] = save

        trie = Trie()
        for w in words:
            trie.insert(w)
        m, n = len(board), len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                dfs(i, j, res, trie.root)
        return res

if __name__ == '__main__':
    """
    题设: 
        二维棋盘上搜索若干字符串, 一个字符不允许被一个单词重复使用.
        79th只搜索一个词. 
    解法1:
        数据结构: 稍微不一样的trie: search的时候需要提供node来加速.
        因为set是无序的, 所以不能用来回复word的值...
        一个关键错误: 在找到一个解之后不能停, 要继续找...
        set初始化是set([(i,j)])...卧槽..
        注意实际上不需要 hasPrefix... 直接在dfs里面写更简单
    解法2:
        用给走过的路用None赋值. 
        trie: 不调用hasPrefix.  在trie的end节点存储word... 这样就不用在dfs里面存了. 
        还有个trick.. 在找到一个之后, 在trie里面把对应的node.word赋值为None. 
    TODO 回溯法
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
