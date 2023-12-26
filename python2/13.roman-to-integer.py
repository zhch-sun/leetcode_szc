#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#
class Solution(object):
    # def romanToInt(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     translations = {
    #         'I': 1,
    #         'V': 5,
    #         'X': 10,
    #         'L': 50,
    #         'C': 100,
    #         'D': 500,
    #         'M': 1000,
    #     }
    #     number = 0
    #     s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
    #     s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
    #     s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
    #     for char in s:
    #         number += translations[char]
    #     return number

    def romanToInt(self, s):
        translations = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        num = 0
        prev = float('inf')
        for char in s:
            cur = translations[char]
            if cur > prev:
                num += cur - 2 * prev
            else:
                num += cur
            prev = cur
        return num

if __name__ == '__main__':
    """
    解法1:
        替换法. 把六种反序情况分别replace。
        这样不用考虑反例顺序，IV和IX不会同时出现。
    解法2:
        scan法. 遇到反序减去2*prev
    scan method is better: 记录之前的char，遇到反例减去2*prev
    """
    s = Solution()
    print(s.romanToInt('MCMXCIV'))

