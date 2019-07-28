#
# @lc app=leetcode id=211 lang=python
#
# [211] Add and Search Word - Data structure design
#

from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isEnd = False

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.root.isEnd = True        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for char in word:
            cur = cur.nodes[char]
        cur.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(word, self.root)

    def match(self, word, root):
        for idx, char in enumerate(word):
            if char != '.':
                root = root.nodes.get(char)
                if root is None:
                    return False
            else:
                new_word = word[idx+1:]
                for node in root.nodes.values():  # for node in root.nodes:  # 这是错解...
                    if self.match(new_word, node):
                        return True
                return False
        return root.isEnd

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    """
    解法1: 遇到'.' 就for循环递归. 把剩下的word和node传进去
    所以需要额外一个函数, 其输入需要有node. 
    Note: 插入时  cur.isEnd = True很容易忘记...
    解法2: iterative: 用stack..
    解法3: python短答案. 其实是用list存着所有可能的值, 用了更多的memory. 
    """
    s = WordDictionary()
    s.addWord("mad")
    s.addWord("dad")
    s.addWord("bad")
    print(s.search("pad"))
    print(s.search("bad"))
    print(s.search(".ad"))
    print(s.search("b.."))

