#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#

import itertools
import re

class Solution(object):
    # def countAndSay(self, n):
    #     """
    #     :type n: int
    #     :rtype: str
    #     """
    #     s = '1'
    #     for _ in range(n - 1):
    #         strList = list()
    #         for digit, group in itertools.groupby(s):
    #             strList.append(str(len(list(group))) + digit)
    #         s = ''.join(strList)
    #     return s

    # def countAndSay(self, n):
    #     s = '1'
    #     for _ in range(n - 1):
    #         s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    #     return s

    def countAndSay(self, n):
        s = '1'
        for _ in range(n - 1):
            strList = []
            count = 1
            for i in range(1, len(s)):
                if s[i - 1] == s[i]:
                    count += 1
                else:
                    strList.append(str(count))
                    strList.append(s[i - 1])
                    count = 1  # Note That!!!!
            strList.append(str(count))  # forget this...
            strList.append(s[-1])
            s = ''.join(strList)
        return s


if __name__ == '__main__':
    """
    解法1:
        for loop solution (无论是for和while都免不了最后两个append)
        双指针? while loop.
    解法2:
        itertools.groupby solution.
    fatest: TODO regular expression results...
    """
    # import itertools
    s = Solution()
    for i in range(10):
        print(s.countAndSay(i+1))

