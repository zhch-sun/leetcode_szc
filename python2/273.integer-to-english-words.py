#
# @lc app=leetcode id=273 lang=python
#
# [273] Integer to English Words
#

# @lc code=start
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def three(a):
            ans = ''
            quo, a = divmod(a, 100)
            if quo:  # 处理百位
                ans += smalls[quo] + ' Hundred' + ('' if not a else ' ')  # 中间的空格还是需要去掉
            if not a:
                return ans
            if a >= 20:  # 处理十位
                quo, a = divmod(a, 10)
                ans += mediums[quo] + ('' if not a else ' ')
            if a:  # 0的时候不做处理
                ans += smalls[a]
            return ans

        bigs = ['', 'Thousand', 'Million', 'Billion']
        mediums = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', \
            'Seventy', 'Eighty', 'Ninety'] # 'Hundred'
        smalls = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', \
            'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',\
                'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',\
                    'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        if not num:
            return smalls[0]
        i = 9
        ans = ''
        while num:
            quo, num = divmod(num, 10 ** i)
            ret = three(quo)
            if ret:
                # if ans:  # 处理第一位的时候..
                ans += ' '  # 导致第一位有空格
                ans += ret + ' ' + bigs[i // 3]  # 最后会有空格
            i -= 3  # Note 不是/=3 !!
        return ans.strip()  # 仍然有空格
        
if __name__ == '__main__':
    """
    分治法. 整数最大20亿. 分成三块, 1-999
    不能处理0的情况.
    注意循环中不是i/=3!!
    """
    s = Solution()
    print(s.numberToWords(123))
    print(s.numberToWords(12345))
    print(s.numberToWords(1234567))
    print(s.numberToWords(1234567891))
# @lc code=end

