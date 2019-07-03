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
        # 那个zigzag的斜线实际上没有意义, 可以看成先竖直向上, 再竖直向下
        # 所以只要记录两个位置调换顺序即可
        # 99.72% 386us a little faster....
        if numRows == 1 or numRows >= len(s):
            return s
        L = [''] * numRows
        # have to initialize -1 for step
        index, step = 0, -1  # step: direction for index
        for x in s:
            L[index] += x
            if index == 0 or index == numRows - 1:
               step = -1 * step
            index += step
                        
        return ''.join(L)


    # def convert(self, s, numRows):
    #     # 99.07?  405 us
    #     # join version
    #     if numRows == 1 or numRows >= len(s):
    #         return s
    #     L = [[] for _ in range(numRows)] 
    #     index, step = 0, -1
    #     for x in s:
    #         L[index].append(x)
    #         if index == 0 or index == numRows - 1:
    #            step = -1 * step
    #         index += step
                        
    #     return ''.join([''.join(item) for item in L])


if __name__ == '__main__':
    """
    
    """
    s = Solution()
    s.convert('PAYPALISHIRING', 3)


