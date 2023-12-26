#
# @lc app=leetcode id=119 lang=python
#
# [119] Pascal's Triangle II
#
class Solution(object):
    # def getRow(self, rowIndex):
    #     """
    #     :type rowIndex: int
    #     :rtype: List[int]
    #     """
    #     row = [1]
    #     for _ in range(rowIndex):
    #         row = [x + y for x, y in zip([0] + row, row + [0])]
    #     return row
    
    # def getRow(self, rowIndex):
    #     # 这个解法应该就不要了.
    #     # 直接初始化一个长row, 而不是[1]
    #     row = [1] * (rowIndex + 1)  #避免了row等于0的情况..  
    #     for i in xrange(2, rowIndex + 1):  # Note start from 2!!
    #         for j in xrange(i - 1, 0, -1):
    #             row[j] += row[j-1]
    #     return row
    
    def getRow(self, rowIndex):
        # 直接初始化一个长row, 而不是[1]
        row = [1] * (rowIndex + 1)  #避免了row等于0的情况..  
        for i in xrange(2, rowIndex + 1):  # Note start from 2!!
            for j in xrange(1, i):
                row[i-j] += row[i-j-1]
        return row
        
if __name__ == '__main__':
    """
    题设: 返回杨辉三角的第k行.
    解法1: 
        offset sum. 两个错开的行相加, 需要concat[0], 不采用
    解法2: 
        用1初始化一个完整长度的array. 循环搞即可. 
        从前向后或者从后向前算均可, 毕竟对称. 
    解法3:
        因为对称性, 可以先生成前一半, 最后对称过去? 
    解法4:
        还有数学大法...
    """
    s = Solution()
    for i in range(5):
        print(s.getRow(i))

