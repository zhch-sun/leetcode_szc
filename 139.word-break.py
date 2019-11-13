#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#
class Solution(object):
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: bool
    #     """        
    #     N = len(s)
    #     wordSet = set(wordDict)
    #     f = [False] * (N + 1)
    #     f[0] = True
    #     for i in xrange(1, N + 1):
    #         for j in xrange(i):  # Note 不能从1开始!!!
    #             if f[j] and s[j:i] in wordSet:  # Note index的对应啊..
    #                 f[i] = True
    #                 break
    #     return f[-1]

    # def wordBreak(self, s, wordDict):
    #     # dp = [True] + [False] * (len(s))  # 这里还真是慢..
    #     N = len(s)
    #     dp = [False] * (N + 1)
    #     dp[0] = True
    #     wordSet = set(wordDict)
    #     sizes = set(map(len, wordSet))  # 统计所有长度!

    #     for i in xrange(1, len(s) + 1): # 注意这里..
    #         for j in sizes:  # 只循环可能的长度.
    #             idx = i - j
    #             if dp[idx] and s[idx:i] in wordSet:
    #                 dp[i] = True
    #                 break
    #     return dp[-1]

    def wordBreak(self, s, wordDict):
        def dfs(i):  # i 还是代表个数最舒服
            if i == 0:
                return True
            if i in f:
                return f[i]
            for sz in sizes:
                j = i - sz
                if j >= 0 and s[j:i] in wordSet and dfs(j):
                    f[i] = True
                    return f[i]
            f[i] = False  # 最好不要在循环前面初始化. 
            return f[i]
        N = len(s)
        wordSet = set(wordDict)
        sizes = set(map(len, wordSet))  # 这里是set
        f = {}
        return dfs(N)

if __name__ == '__main__':
    """
    题设: 一个"非空"字符串被"非空"字典里的字符串完全表达, 不能重叠, 字典可用多次.
    解法1: 
        dp: 标记每个位置是否有以当前位置结尾的解. 
        set是神来之笔. 把每个索引加速到o(1)!
        内环中, j是初始, i是后面, 需要非常注意索引才能不出错.
    解法2: 
        优化: 可以循环j也可以循环word. 可以统计所有的word的长度, set之后.
            只循环字典里有的长度. 比循环j和循环word都快!
    解法3: 
        记忆化搜索理论上更快: 因为可以过滤不需要的步骤.
    TODO trie可以帮忙? how?
    """
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))
    print(s.wordBreak("applepenapple", ["apple", "pen"]))
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
