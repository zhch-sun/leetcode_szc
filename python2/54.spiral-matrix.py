#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
class Solution(object):
    # def spiralOrder(self, matrix):
    #     """
    #     :type matrix: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     if not matrix or not matrix[0]:
    #         return []
    #     res = list(matrix.pop(0)) + \
    #         self.spiralOrder(zip(*matrix)[::-1])
    #     return res

    # def spiralOrder(self, matrix):
    #     return matrix and list(matrix.pop(0)) + \
    #         self.spiralOrder(zip(*matrix)[::-1])
    
    # def spiralOrder(self, matrix):
    #     if not matrix or not matrix[0]:
    #         return []
    #     M, N = len(matrix), len(matrix[0])
    #     dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
    #     idx = 0  # 当前dirs的指针
    #     i, j = 0, 0
    #     ans = []
    #     for _ in xrange(M * N):  # 不需要while
    #         ans.append(matrix[i][j])
    #         matrix[i][j] = None
    #         ni = i + dirs[idx][1]
    #         nj = j + dirs[idx][0]
    #         if 0 <= ni < M and 0 <= nj < N and \
    #             matrix[ni][nj] is not None:
    #             i, j = ni, nj  # Note更新!
    #         else:
    #             idx = (1 + idx) % 4  # 这个更新方式!
    #             i = i + dirs[idx][1]
    #             j = j + dirs[idx][0]
    #     return ans

    # def spiralOrder(self, matrix):
    #     if not matrix:
    #         return []
    #     res = []
    #     nc = len(matrix[0])
    #     nr = len(matrix)
    #     dc, dr = 1, 0
    #     ic, ir = 0, 0
    #     for _ in xrange(nc * nr):
    #         res.append(matrix[ir][ic])
    #         matrix[ir][ic] = None
    #         # 注意需要mod防止越界. 在0处会变成-1, 对称的位置肯定已经是None了.
    #         if matrix[(ir+dr)%nr][(ic+dc)%nc] == None:  # Note %号。。。
    #             # 这个公式背后实际是线性代数的旋转矩阵. 
    #             # 将向量顺时针旋转九十读
    #             dc, dr = -dr, dc
    #         ic += dc
    #         ir += dr
    #     return res

    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return None
        M, N = len(matrix), len(matrix[0])
        i, j = 0, -1  # Note -1是精髓...
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        idx = 0
        steps = [N, M - 1]
        ans = []  # 初始位置不能放 m[0][0]
        while steps[idx % 2]:  # 条件下一个step不为0
            dj, di = dirs[idx]
            for _ in xrange(steps[idx % 2]):  # %2
                i += di
                j += dj
                ans.append(matrix[i][j])
            steps[idx % 2] -= 1  # 时刻不忘%2..
            idx = (idx + 1) % 4
        return ans

if __name__ == '__main__':
    """
    解法1/ 解法2:
        先pop第一行, 再矩阵逆时针转, 再pop第一行....
        同48题, 逆时针转这个操作可以分解为 zip + [::-1]
        而且必须convert成list, 而且还不能在zip外面convert.
        是因为zip的返回值是list of tuple...
    解法2:
        讨论两种情况!
        输入是[]时, matrix相当与False, 但return matrix就是return []
        输入是[[]], matrix是True, 但是pop(0)后变成了[], 而 [] + [] 还是 []
    解法3:
        迭代位置而不是行, 用记录走过的路径和M*N比较. 
        修改原matrix赋值None或者用bool矩阵. 
        注意区分ni nj和i, j.... 
        注意idx的更新方式!
    解法4:
        若干trick. 
        旋转规律: di, dj = dj, -di: 可以不用dirs.(旋转矩阵)
        边界只需要检查None, 因为对称性. 
    解法5: 
        不需要修改matrix或者额外空间.
        发现每次步长都减一. 
        精髓是初始化时候的-1, 时刻不能忘mod2, mod4
    """
    s = Solution()
    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
    # matrix = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8,9]
    # ]    
    print(s.spiralOrder(matrix))

