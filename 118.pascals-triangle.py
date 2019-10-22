#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#
class Solution(object):
    # def generate(self, numRows):
    #     """
    #     :type numRows: int
    #     :rtype: List[List[int]]
    #     """
    #     if numRows == 0:
    #         return []
    #     res = [[] for _ in range(numRows)]
    #     res[0] = [1]
    #     for i in range(1, numRows):
    #         res[i].append(1)
    #         for j in range(1, i):
    #             res[i].append(res[i-1][j-1] + res[i-1][j])
    #         res[i].append(1)
    #     return res

    def generate(self, numRows):
        res = [[1] * (i+1) for i in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res

if __name__ == '__main__':
    """
    题设: 给行数, 生成整个三角
    解法1: 我的for循环还是复杂
    解法2: 用1初始化整个三角可以避免很多逻辑....
    其他解法:
        1. list comprehension: 需要concat头尾,O(n)? 反正是慢
        2. offset sum: 用map和lambda做向量加法, 中间还是要concat, 慢;
    """
    s = Solution()
    print(s.generate(5))
