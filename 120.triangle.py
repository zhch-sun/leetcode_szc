#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        res = triangle[-1]
        for i in xrange(len(triangle) - 2, -1, -1):
            for j, row in enumerate(triangle[i]):
                res[j] = min(res[j], res[j+1]) + row  # it's not row[j]
        return res[0]

if __name__ == '__main__':
    """
    题设: 给定一个三角形array of array, 找到从上到下的最短路
    解法: dp...
    """
    s = Solution()
    array = [
               [2],
              [3,4],
             [6,5,7],
            [4,1,8,3]
            ]
    print(s.minimumTotal(array))


