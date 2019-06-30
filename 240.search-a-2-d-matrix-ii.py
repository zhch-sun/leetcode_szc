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
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col > -1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

if __name__ == '__main__':
    """
    这个题从右上开始做, 像个tree一样. 左下角的一定小于上面,右下角一定大于. 
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
