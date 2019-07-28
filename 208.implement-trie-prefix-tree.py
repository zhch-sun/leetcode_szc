#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.isWord = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()  # the 
        self.root.isWord = True

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for char in word:
            # 因为defaultdict, 所以下面两句不用写.
            # if char not in cur.nodes:
            #     cur.nodes[char] = TrieNode()
            cur = cur.nodes[char]
        cur.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            cur = cur.nodes.get(char)
            if cur is None:
                return False
            # if char in cur.nodes:  # 用get!
            #     cur = cur.nodes[char]
            # else:
            #     return False
        return cur.isWord

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
    因为指针本身已经决定了node的值, 所以node中只需要额外的一个bool去存储这里是否是leaf
    用字典做映射比array存指针要省显存. 
    细节1:已经用了defaultdict, 所以初始化的时候很简单
    细节2:这个题应该用get()函数而不是in来判断是否存在, 因为我还需要dict内的元素. 
    细节3:理论上search和startsWith里面有一段可以抽出来单独一个函数, 但是我不想写. 
    """
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))
