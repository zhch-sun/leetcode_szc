#
# @lc app=leetcode id=1032 lang=python
#
# [1032] Stream of Characters
#

# @lc code=start
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isEnd = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def put(self, word):
        cur = self.root
        for char in word:
            cur = cur.nodes[char]
        cur.isEnd = True
    
    def get_any(self, word):
        cur = self.root
        for char in word:
            cur = cur.nodes.get(char, None)  # 错了..
            if not cur:
                return False
            if cur.isEnd:
                return True
        # return cur.isEnd  # word不为空

    def prefix(self, char, root):
        return root.nodes.get(char, None)

# class StreamChecker(object):
#     # TLE... 必须优化的很好才能不超时
#     def __init__(self, words):
#         """
#         :type words: List[str]
#         """
#         self.trie = Trie()
#         self.pts = []  # 当前有效的指针
#         for w in words:
#             self.trie.put(w)

#     def query(self, letter):
#         """
#         :type letter: str
#         :rtype: bool
#         """
#         new_pts = []
#         self.pts += [self.trie.root]
#         ans = False
#         for p in self.pts:
#             p = self.trie.prefix(letter, p)
#             if p:
#                 new_pts.append(p)
#                 if p.isEnd:
#                     ans = True
#         self.pts = new_pts  # 忘记了
#         return ans

class StreamChecker(object):
    def __init__(self, words):
        self.trie = Trie()
        self.s = ''
        for w in words:
            self.trie.put(reversed(w))  # 后缀树

    def query(self, letter):
        self.s = letter + self.s
        return self.trie.get_any(self.s)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# @lc code=end
if __name__ == '__main__':
    """
    解法1: TLE
        前缀树, 维护一个当前有效的指针数组. 
        但是无法快速处理 aaaaa这样的输入. 会变成N^2
        所以超时.
    解法2:
        后缀树. 即把words反向插入树中. 这样不需要self.pts
        对于aaaa, 理论复杂度还是n2, 但是常数小了, 只调一次函数
        对于aaab, 则完美解决.
        对于baaa, 还是慢.
    解法2:
        自动机, 未看
    """
    s = StreamChecker(["cd","f","kl"])
    print(s.query('a'))
    print(s.query('b'))
    print(s.query('c'))
    print(s.query('d'))
    print(s.query('e'))
    print(s.query('f'))
    print(s.query('g'))
    print(s.query('h'))
    print(s.query('k'))
    print(s.query('l'))
    
    

