#
# @lc app=leetcode id=166 lang=python
#
# [166] Fraction to Recurring Decimal
#
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # zero numerator
        if numerator == 0: 
            return "0"
        # Note 括号!!
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''  
        num, den = abs(numerator), abs(denominator)
        # 整数部分
        n, remain = divmod(num, den)  # obtain integral part
        ret = sign + str(n)
        if remain == 0:
            return ret
        # 小数部分
        ret += '.'
        cache = {}
        idx = len(ret)
        while remain != 0:
            cache[remain] = idx  # 必须要调到上边来.. 最重要的trick. 
            remain *= 10
            n, remain = divmod(remain, den)
            ret += str(n)
            if remain in cache:
                return ret[:cache[remain]] + '(' + ret[cache[remain]:] + ')'
            idx += 1
        return ret

        
if __name__ == '__main__':
    """
    1. 需要各种各样的分类讨论...
    2. 最重要的细节是了解
        1. cache里面是remain. 
        2. 循环最开始就要把remain加到cache里.前面算出的remain仍要利用上. 
    """
    s = Solution()
    # print(float(-2) / 7)
    print(s.fractionToDecimal(1, 4))
    print(s.fractionToDecimal(1, 333))
    print(s.fractionToDecimal(-9, 7))
        

