#
# @lc app=leetcode id=648 lang=python
#
# [648] Replace Words
#

# @lc code=start
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
    def get_any(self, word):
        cur = self.root
        for char in word:
            cur = cur.nodes.get(char, None)
            if not cur:
                return False
            if cur.val:
                return cur.val

class Solution(object):
    def replaceWords(self, words, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for w in words:
            trie.put(w)
        ans = []
        for w in sentence.split(' '):
            ret = trie.get_any(w)
            if ret:
                ans.append(ret)
            else:
                ans.append(w)
        return ' '.join(ans)

if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.replaceWords(["cat", "bat", "rat"], \
        "the cattle was rattled by the battery"))
# @lc code=end

