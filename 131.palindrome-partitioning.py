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
    #     # 83 %  83%
    #     def dfs(res, tmp, s, start):
    #         if start == len(s):
    #             res.append(tmp[:])
    #         for i in range(start, len(s)):
    #             if self.isPal(s, start, i):
    #                 tmp.append(s[start:i+1])
    #                 dfs(res, tmp, s, i+1)
    #                 tmp.pop()
    
    #     res = []
    #     tmp = []
    #     dfs(res, tmp, s, 0)
    #     return res

    # def isPal(self, s, left, right):
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True

    def partition(self, s, set_pal=set(), dp={}):
        # 98% 5%
        if not s:
            return None
        if s in dp:
            return dp[s]  # 真的会有这种情况, 重要加速

        res_list = []
        for i in range(1, len(s) + 1):  # Note len(s) + 1....
            left = s[:i]
            if left in set_pal or left == left[::-1]:
                set_pal.add(left)
                right = s[i:]  # Note s[3:] 这种是 '' 3可以超过len(s)
                ret = self.partition(right, set_pal, dp)
                if ret is not None:
                    for i in ret:
                        res_list.append([left] + i)
                else:  # right is []
                    res_list.append([left])
        dp[s] = res_list
        return dp[s]

if __name__ == '__main__':
    """
    就是backtrack. 要想到怎么去穷举. 
    bp: 注意真的会用到之前的dp[s]. 
    """
    s = Solution()
    print(s.partition('aab'))
