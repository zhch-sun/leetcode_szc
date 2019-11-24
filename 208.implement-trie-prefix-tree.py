#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

from collections import defaultdict

# class TrieNode(object):
#     def __init__(self):
#         self.nodes = [None] * 26
#         self.isEnd = False

# class Trie(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()  # the 
#       # self.root.isEnd = True  # 这个初始化用不到.

#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: None
#         """
#         cur = self.root
#         for char in word:
#             idx = ord(char) - ord('a')
#             if cur.nodes[idx] is not None:
#                 cur = cur.nodes[idx]
#             else:
#                 cur.nodes[idx] = TrieNode()
#                 cur = cur.nodes[idx]
#         cur.isEnd = True

#     def search(self, word):
#         """
#         Returns if the word is in the trie.
#         :type word: str
#         :rtype: bool
#         """
#         cur = self.root
#         for char in word:
#             cur = cur.nodes[ord(char) - ord('a')]
#             if cur is None:
#                 return False
#         return cur.isEnd

#     def startsWith(self, prefix):
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         :type prefix: str
#         :rtype: bool
#         """
#         cur = self.root
#         for char in prefix:
#             cur = cur.nodes[ord(char) - ord('a')]
#             if cur is None:
#                 return False
#         return True

class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isEnd = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()  # the 
        # self.root.isEnd = True

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for char in word:
            cur = cur.nodes[char]  # 所以defaultdict
        # cur.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            cur = cur.nodes.get(char)  # 用get
            if cur is None:
                return False
        return cur.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for char in prefix:
            cur = cur.nodes.get(char)
            if cur is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    """
    解法1:
        hash存储指针.
        用字典做映射比array存指针要省内存. 
        也可以在node的字典中加一个特殊字符比如'#'来判断是否是leaf.
        细节:
            已经用了defaultdict, 所以初始化的时候很简单
            这个题应该用get()函数而不是in来判断是否存在, 因为我还需要dict内的元素. 
            理论上search和startsWith里面有一段可以抽出来单独一个函数, 但是我不想写. 
    解法2:
        标准解法, 26叉树. 插入的时候更麻烦. 
    """
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
