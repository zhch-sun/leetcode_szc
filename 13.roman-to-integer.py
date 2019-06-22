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
    replace method: the order of replace? 
    scan method is better: 
    """
    s = Solution()
    print(s.romanToInt('MCMXCIV'))

