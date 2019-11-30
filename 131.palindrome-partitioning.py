#
# @lc app=leetcode id=131 lang=python
#
# [131] Palindrome Partitioning
#
class Solution(object):
    # def partition(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[List[str]]
    #     """    
    #     def dfs(tmp, s):
    #         if s == '':
    #             ans.append(tmp[:])
    #             return
    #         for i in xrange(1, len(s) + 1):  # len(s) + 1
    #             left = s[:i]
    #             if left == left[::-1]:
    #                 tmp.append(left)
    #                 dfs(tmp, s[i:])
    #                 tmp.pop()
    #         return

    #     ans = []
    #     dfs([], s)
    #     return ans

    def partition(self, s):
        def dfs(s):  # Note 整个没有tmp了!!!
            if s == '':
                return [[]]  # Note!!
            if s in f:
                return f[s]
            ans = []
            for i in xrange(1, len(s) + 1):  # len(s) + 1
                left = s[:i]
                if left == left[::-1]:
                    ret = dfs(s[i:])
                    for item in ret:
                        ans.append([left] + item)  # 没有tmp了..
            f[s] = ans
            return f[s]

        f = {}
        return dfs(s)

if __name__ == '__main__':
    """
    解法1:
        dfs, Note不要用循环来判断回文...太慢了
    解法2:
        记忆化搜索
    """
    s = Solution()
    print(s.partition('aab'))
