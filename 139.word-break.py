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
    #     dp = [True] +  [False] * (len(s))
    #     wordSet = set(wordDict)
    #     for i in range(1, len(s) + 1): # 注意这里..
    #         for j in range(i):
    #             if dp[j] and s[j:i] in wordSet:
    #                 dp[i] = True
    #                 break
    #     return dp[-1]

    def wordBreak(self, s, wordDict):
        # dp = [True] + [False] * (len(s))  # 这里还真是慢..
        dp = [False] * (len(s) + 1)
        dp[0] = True
        maxLength = max(map(len, wordDict + ['']))  # 需要处理wordDict为空的情况
        wordSet = set(wordDict)
        for i in range(1, len(s) + 1): # 注意这里..
            start = max(i - maxLength, 0)
            for j in range(start, i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]

if __name__ == '__main__':
    """
    解法1: dp: 标记每个位置是否有以当前位置结尾的解. 
        内环中, j是初始, i是后面 [j, i)是当前位置, 所以i的range需要是(1, len(s) + 1)
        而且需要dp[0]一直是True. 所以必须前面有一个[True]
    解法2: dp加速
        1. 加入一个maxLength用来控制循环大小
        2. dp初始化的时候不用list concat. 
    TODO dfs尽管不快, 但还是要理解. 
    """
    s = Solution()
    print(s.wordBreak("leetcode", ["leet", "code"]))
    print(s.wordBreak("applepenapple", ["apple", "pen"]))
    print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
