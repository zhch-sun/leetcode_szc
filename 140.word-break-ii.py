#
# @lc app=leetcode id=140 lang=python
#
# [140] Word Break II
#

# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def dfs(i):  # [1, N]
            if i == 0:
                return [[]]  # szc 注意这个初始化 
            if i in f:
                return f[i]
            ans = []
            for sz in sizes:
                j = i - sz
                word = s[j:i]
                if j >= 0 and word in wordSet and dfs(j):
                    # 不能写f[j], i==0的情况...
                    ans += [n + [word] for n in dfs(j)]  
            f[i] = ans
            return f[i]
            
        N = len(s)
        wordSet = set(wordDict)
        sizes = set(map(len, wordSet))
        f = {}
        ans = dfs(N)
        return [' '.join(n) for n in ans]

if __name__ == '__main__':
    """
    题设, 返回所有的组合方案, 需要加上空格组成完整字符串
    解法1:
        记忆化搜索, O(N * len(sizes))
    解法2:
        dp, 不管: dfs更快
    """
    s = Solution()
    print(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) 
    print(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) 
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) 
# @lc code=end

