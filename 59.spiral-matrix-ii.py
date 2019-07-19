#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 99.82%
        res = [[0] * n for _ in range(n)]
        ic, ir = 0, 0
        dc, dr = 1, 0
        for item in range(1, n * n + 1):
            res[ir][ic] = item
            if res[(ir + dr) % n][(ic + dc) % n] > 0:
                dc, dr = -dr, dc
            ic += dc
            ir += dr
        return res

if __name__ == '__main__':
    """
    1. 简单解法:
    这题应该是不能用recursion了.. 
    需要inside-out 从里向外一层层加数字. 仍然用矩阵旋转
    2. walk the spiral
    """
    s = Solution() 
    print(s.generateMatrix(3))

