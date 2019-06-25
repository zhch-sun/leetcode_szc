#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
class Solution(object):
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     start = 0
    #     end = 0
    #     for i in xrange(len(s)):  # note this should be xrange
    #         start, end = self.helper(s, i, i, start, end)
    #         start, end = self.helper(s, i, i + 1, start, end)
    #     return s[start:end]

    # def helper(self, s, l, r, start, end):  # l, r is the center
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         l -= 1
    #         r += 1
    #     # return s[l+1:r]  # this is actually O(n)!!!
    #     if r - (l + 1) > end - start:
    #         start = l + 1  # note this
    #         end = r  # Note this
    #     return start, end  # use less return in function

    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False] * len(s) for _ in xrange(len(s))]  # Note this!
        start = end = 0
        for i in xrange(n - 1, -1, -1):  # Note n-1!!!
            for j in xrange(i, n):
                dp[i][j] = True if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]) else False
                if dp[i][j] and j - i > end - start:
                    start = i
                    end = j  # Note end is included!
        return s[start:end + 1]


if __name__ == '__main__':
    """
    brute force. Note string copy makes it O(n3)
    2D-DP!: 参见 leetcode 答案 (比较慢)
    还是比较优雅 dp[i, j] 意味着 i到j之间是回文. 然后用dp[i-1, j+1]作为子任务. 
    这样做问题是要保证循环时dp[i-1, j+1]存在, 所以i循环时递减, j递增...
    注意: geeksforgeeks的题目不一样! 1.子串内的字符不需要紧挨着.. 2.只需要返回最大值, 不需要前后位置.
    Manacher algorithm https://www.hackerearth.com/zh/practice/algorithms/string-algorithm/manachars-algorithm/tutorial/
    https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
    leetcode答案里还有个链接...
    """
    s = Solution()
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome('cbbd'))
    print(s.longestPalindrome('dakffdadff'))

