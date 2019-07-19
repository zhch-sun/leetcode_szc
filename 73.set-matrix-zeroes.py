#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#
class Solution(object):
    # def setZeroes(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: None Do not return anything, modify matrix in-place instead.
    #     """
    #     if not matrix:
    #         return
    #     rows, cols = set(), set()
    #     m, n = len(matrix), len(matrix[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 rows.add(i)
    #                 cols.add(j)
    #     for r in rows:
    #         matrix[r] = [0] * n
    #     for c in cols:
    #         for i in range(m):
    #             matrix[i][c] = 0
    #     return matrix

    # def setZeroes(self, matrix):
    #     if not matrix:
    #         return
    #     col0 = 1
    #     m, n = len(matrix), len(matrix[0])
    #     for i in range(m):
    #         for j in range(n):  # 可以改成从1开始循环, 这样避免掉后面的判断...
    #             if matrix[i][j] == 0:
    #                 matrix[i][0] = 0
    #                 if j != 0:
    #                     matrix[0][j] = 0  # 这个赋值必须在 j!=0内...
    #                 else:
    #                     col0 = 0
    #     for i in range(1, m):
    #         if matrix[i][0] == 0:
    #             matrix[i] = [0] * n
    #     for j in range(1, n):
    #         if matrix[0][j] == 0:
    #             for i in range(m):
    #                 matrix[i][j] = 0
    #     if matrix[0][0] == 0:
    #         matrix[0] = [0] * n
    #     if col0 == 0:
    #         for i in range(m):
    #             matrix[i][0] = 0
    #     return matrix

    def setZeroes(self, matrix):
        if not matrix:
            return
        col0 = 1
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1, n):  # 可以改成从1开始循环, 这样避免掉后面的判断...
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0  # 这个赋值必须在 j!=0内...
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        return matrix

if __name__ == '__main__':
    """
    第一种做法是o(m+n)的空间复杂度
    第二种在行和列的头上赋值为0, 因为(0,0)点有两个信息所以额外拿出一个变量来记录第一列.
    非常复杂. 在赋值完毕准备 给所有位置赋0的时候, 第一行和第一列先不能动..否则会导致全0. 
    所以官方答案第二步是倒着循环赋值的...厉害呀... 第一步修改了循环范围．．．厉害．．
    """
    s = Solution()
    matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
    ]
    # matrix = [
    #     [1,1,1],
    #     [0,1,2]
    # ]    
    print(s.setZeroes(matrix))
