#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#
class Solution(object):
    def intToRoman(self, num):
        # 375 us
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i = 0
        ans = ''
        while num:  # 里面套for循环会慢.
            if num >= values[i]:
                ans += romans[i]
                num -= values[i]
            else:
                i += 1
        return ans

if __name__ == '__main__':
    """
    1. 最简单的查表法是: 对千位,百位,十位,个位的每一种(10种)情况查表. 
    2. 查表法2, 列出罗马字符本身的钱数情况(1,4,5,9,10), 然后递减num
    """
    s = Solution()
    print(s.intToRoman(3999))
    print(s.intToRoman(1994))

