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
    #     if not matrix:
    #         return []
    #     res = list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
    #     return res

    # def spiralOrder(self, matrix):
    #     return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])

    # def spiralOrder(self, matrix):
    #     # 不修改matrix的唯一解法？
    #     dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))  # (col, row) (x, y)
    #     res = []
    #     if not matrix:
    #         return matrix  # 因为后面有matrix[0], 只能先判断
    #     nC = len(matrix[0])  # num of col
    #     nR = len(matrix)  # num of row

    #     nSteps = [nC, nR-1]  # 还只能这样初始化, 因为每次路径比原先短1
    #     idx = 0  # index of direction
    #     ir = 0  # index of row
    #     ic = -1  # index of column
    #     while nSteps[idx%2] > 0:  # Note 这个条件只能这么写, 当前这个idx的steps为0！！
    #         for _ in range(nSteps[idx % 2]):
    #             ic += dirs[idx][0]
    #             ir += dirs[idx][1]
    #             res.append(matrix[ir][ic])
    #         # 下面两句话的顺序
    #         nSteps[idx % 2] -= 1
    #         idx = (idx + 1) % 4
    #     return res
    
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        res = []
        nc = len(matrix[0])
        nr = len(matrix)
        dc, dr = 1, 0
        ic, ir = 0, 0
        for _ in xrange(nc * nr):
            res.append(matrix[ir][ic])
            matrix[ir][ic] = None
            # 注意需要mod防止越界. 在0处会变成-1, 对称的位置肯定已经是None了.
            if matrix[(ir+dr)%nr][(ic+dc)%nc] == None:  # Note %号。。。
                # 这个公式背后实际是线性代数的旋转矩阵. 
                # 将向量顺时针旋转九十读
                dc, dr = -dr, dc
            ic += dc
            ir += dr
        return res

    # def spiralOrder(self, matrix):
    #     # 这个解法需要太多细节了. 
    #     if not matrix:
    #         return []
    #     res = []
    #     nc = len(matrix[0])
    #     nr = len(matrix) - 1
    #     dc, dr = 1, 0
    #     ic, ir = -1, 0
    #     while True:
    #         if dc != 0:
    #             # 不能这样写... 不能把正负时候的情况合并, 需要调换:前后的顺序
    #             # 可以找到两个数中间的大小, swap一下. 但是还是很麻烦. 
    #             res += matrix[ir][ic+dc:ic+dc*(nc+1):dc]
    #             ic += dc * nc
    #             nc -= abs(dc)
    #             if nr == 0:
    #                 break
    #         else:
    #             # python 不支持二维时候row的:select....
    #             # res += matrix[ir+dr:ir+dr*(nr+1):dr][ic]
    #             res += [row[ic] for row in matrix[ir+dr:ir+dr*(nr+1):dr]]
    #             ir += dr * nr 
    #             nr -= abs(dr)
    #             if nc == 0:
    #                 break
    #         dc, dr = -dr, dc
    #     return res


if __name__ == '__main__':
    """
    解法1
    一个简单解法是先pop第一行, 再矩阵逆时针转, 再pop第一行....
    同48题, 逆时针转这个操作可以分解为 zip + [::-1]
    而且必须convert成list, 而且还不能在zip外面convert.
    是因为zip的返回值是list of tuple... 而我不能直接把里面的东西list掉....
    解法2:
    输入是[]时, matrix相当与False, 但return matrix就是return []
    输入是[[]], matrix是True, 但是pop(0)后变成了[], 而 [] + [] 还是 []
    解法3:
    naive的解法,记录两对个的begin和end, 然后外面一个循环, 里面四个循环
    解法4:
    发现每次步长都减一. 
    用direction matrix和nSteps存储 action. 
    解法5:
    发现旋转方向有规律: di, dj = dj, -di. 所以甚至都不用dirs.
    这个实际上就是线性代数的旋转矩阵. 
    另外他这个只要一个循环就可以, 因为把走过的地方写了None.
    解法6:
    无法实现vector的赋值.. 需要各种分类讨论. 不写了. 
    """
    s = Solution()
    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
    matrix = [
    [1, 2, 3],
    [5, 6, 7],
    [9,10,11]
    ]    
    # matrix = [[]]
    # matrix = []
    print(s.spiralOrder(matrix))

