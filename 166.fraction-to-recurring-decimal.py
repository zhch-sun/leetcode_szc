#
# @lc app=leetcode id=166 lang=python
#
# [166] Fraction to Recurring Decimal
#
class Solution(object):
    def fractionToDecimal(self, nume, denom):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # zero numerator
        if nume == 0: 
            return "0"
        # Note 括号!!
        sign = '-' if (nume < 0) ^ (denom < 0) else ''  
        num, den = abs(nume), abs(denom)
        # 整数部分
        n, remain = divmod(num, den)  
        ret = sign + str(n)
        if remain == 0:
            return ret
        # 小数部分
        ret += '.'
        cache = {}
        idx = len(ret)
        while remain != 0:
            cache[remain] = idx  # Note 必须要调到上边来
            remain *= 10
            n, remain = divmod(remain, den)
            ret += str(n)
            if remain in cache:
                return ret[:cache[remain]] + \
                    '(' + ret[cache[remain]:] + ')'
            idx += 1
        return ret

if __name__ == '__main__':
    """
    题设: 给定分子分母, 返回小数, 循环小数包含在括号里.
    解法:
        需要各种各样的分类讨论...
        最重要的细节是:
            cache里面是remain. 
            循环最开始就要把remain加到cache里.前面算出的remain仍要利用上. 
    """
    s = Solution()
    # print(float(-2) / 7)
    print(s.fractionToDecimal(1, 4))
    print(s.fractionToDecimal(2, 9))
    print(s.fractionToDecimal(1, 333))
    print(s.fractionToDecimal(-9, 7))      
