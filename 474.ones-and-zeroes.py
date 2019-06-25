#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # the max #strings with i 0's and j 1's
        dp = [[0] * (n + 1) for i in range(m + 1)] 

        for s in strs:
            num0 = s.count('0')
            num1 = s.count('1')
            # 循环的时候一个str是可以被用多次的.但仍然要反着循环防止多加.
            for i in range(m, num0 - 1, -1):
                for j in range(n, num1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-num0][j-num1] + 1)
        return dp[m][n]
        
if __name__ == '__main__':
    """
    TODO 速度只有77%? 还有更快的算法?
    """
    s = Solution()
    print(s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
