#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#
class Solution(object):
    # def rotate(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: None Do not return anything, modify matrix in-place instead.
    #     """
    #     n = len(matrix)
    #     A = matrix
    #     for i in xrange(n // 2):  # rows
    #         # 列的旋转区间非常tricky. 首先是n-1而不是n.
    #         # 其次是从i到n-1-i
    #         for j in xrange(i, n - 1 - i):
    #             # 注意顺序
    #             A[j][~i], A[~i][~j], A[~j][i], A[i][j] = \
    #                 A[i][j], A[j][~i], A[~i][~j], A[~j][i] #下面这个是四个点，依次赋值到上面去
    #         # break
    #     # return m 

    # def rotate(self, matrix):
    #     n = len(matrix)
    #     A = matrix
    #     A.reverse()  # this is inplace reverse
    #     print(A)
    #     for i in range(1, n):
    #         for j in range(i):  # 下三角更简单一些..
    #             A[i][j], A[j][i] = A[j][i], A[i][j]
    #     return A 

    def rotate(self, A):
        A[:] = zip(*A[::-1])  # 注意zip的返回值是list of tuple! TODO 加一个map(list, A)?
        
if __name__ == '__main__':
    """
    TODO 非方阵?
    1.我的思路是: 每个边上对应位置的四个元素一起rotate. 注意对称元素的取法：通过取反～！！！
    另外我的i,j的range和python答案不一样. 
    python的~是补码, 即-(x+1)
    2. filp+transpose. 两个顺序决定是顺时针还是逆时针. python可以inplace reverse. 
    3. 用zip竟然可以transpose....震惊了X.  注意zip就是transpose. [::-1]的位置不同变成顺时针转还是逆时针转
    4. 也可以numpy
    """
    s = Solution()
    # matrix = \
    # [
    #     [1,2,3],
    #     [4,5,6],
    #     [7,8,9]
    # ]
    matrix = \
    [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    print(s.rotate(matrix))
