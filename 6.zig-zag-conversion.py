#
# @lc app=leetcode id=6 lang=python
#
# [6] ZigZag Conversion
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """        
        ans = [''] * numRows
        pos = 0
        step = 1
        for char in s:
            ans[pos] += char
            if pos + step < 0 or pos + step >= numRows:
                step *= -1
            pos += step
        return ''.join(ans)

if __name__ == '__main__':
    """
    解法1:
        模拟. 找到上升下降的位置, 逐个填充字符.
        那个zigzag的斜线实际上没有意义, 可以看成先竖直向上, 再竖直向下
        所以只要记录两个位置调换顺序即可
    解法2: 
        找规律
        上下是等差数列.
        中间是等差数列交错的形态. 利用等差数列直接生成. 
    """
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))


