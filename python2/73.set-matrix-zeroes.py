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
            if matrix[i][0] == 0:  # 如果第一列为0, 对应行的flag很自然, 再给col0赋值
                col0 = 0
            for j in range(1, n):  # 从1开始循环, 这样避免掉后面的判断; 其实解法2这里更好
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        return matrix

if __name__ == '__main__':
    """
    解法1: 通过两个set记录为0的行列. o(m+n)的空间复杂度,
    解法23:
    标记阶段:
        二种在行和列的头上赋值为0, 用来当作该行或者列为0的flag, 这样就不需要额外空间
        但是(0,0)点有两个信息所以需要一个变量来记录第一行或者列的状态.
        这里for循环有两种写法:
        解法2的方式更清晰直观, 就是对列的情况进行判断
        解法3更短但是不推荐
    赋值阶段:
        解法2: 第一行和第一列先不能动..否则会导致全0. 
            所以从第二行第二列开始往后搞. 最后再搞第一行第一列.
            复杂度是o(kn), k是0的个数. 适合0比较稀疏的情况
        解法3: 
            从后向前遍历整个矩阵循环赋值. 这样写起来更简单, 但复杂度是o(n2)
            但是从locality的角度更好.
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
