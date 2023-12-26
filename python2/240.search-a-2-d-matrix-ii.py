#
# @lc app=leetcode id=240 lang=python
#
# [240] Search a 2D Matrix II
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        if not matrix or not matrix[0]:
            return False
        M = len(matrix)
        N = len(matrix[0])
        i, j = 0, N - 1
        while i < M and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False

if __name__ == '__main__':
    """
    题设: 
        矩阵 从左到右升序, 从上到下升序, 搜索一个数
        74题前置
    解法: 
        从左上角拎起来是一个堆!, 右上角是一个树BST.
    """
    s = Solution()
    array = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
    print(s.searchMatrix(array, 20))
    print(s.searchMatrix(array, 5))
