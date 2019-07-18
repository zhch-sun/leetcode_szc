#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        res = [0 for _ in range(m + n)]  # total digits 
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                p1 = i + j + 1 # position
                p2 = i + j  # carry
                cur = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                total = res[p1] + cur
                res[p1] = total % 10
                res[p2] += total // 10  # Note this is +=!!!!!!
        res = ''.join(map(str, res))
        res = res.lstrip('0')
        return res if res else '0'

if __name__ == '__main__':
    """
    需要自己实现一个乘法...
    漂亮的图解 https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
    """
    s = Solution()
    print(s.multiply('0', '99'), 99 * 99)
