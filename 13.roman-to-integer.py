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
        """
        :type s: str
        :rtype: int
        """
        translations = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        number = 0
        prev = 2 ** 31
        for cur in s:
            num = translations[cur]
            number += num
            if num > prev:
                number -= 2 * prev
            prev = num
        return number 

if __name__ == '__main__':
    """
    replace method: 把六种情况分别replace。不用考虑反例顺序，IV和IX不会同时出现。
    scan method is better: 记录之前的char，遇到反例减去2*prev
    """
    s = Solution()
    print(s.romanToInt('MCMXCIV'))

