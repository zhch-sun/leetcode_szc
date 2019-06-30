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
    1. 我的for循环: 用1初始化可以避免很多逻辑....
    2. list comprehension: 需要concat头尾,O(n)
    2. offset sum: 用map和lambda做向量加法, 中间还是要concat
    """
    s = Solution()
    print(s.generate(5))



