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
    简单做法是offset sum. 靠concat的
    省内存做法:
    1, 初始化一个完整长度的length
    2. 用之前的生成新的. 内环可以从后向前搞, 也可以从前向后搞. increment更快???
    还有数学大法...
    """
    s = Solution()
    for i in range(5):
        print(s.getRow(i))

