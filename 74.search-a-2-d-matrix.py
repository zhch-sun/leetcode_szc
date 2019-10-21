#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#
import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:  # Note 两种都要写...
            return False
        M, N = len(matrix), len(matrix[0])
        lo, hi = 0, M * N - 1
        while lo <= hi:  # invariant [lo, hi] 有可能没有值
            mid = lo + (hi - lo) // 2
            i, j = divmod(mid, N)  # Note N
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False

if __name__ == '__main__':
    """
    理解题意:
        不是行列都递增, 而是更严格的下面一行第一个大于上面一行最后一个.
        相当于一个递增array拆成了一个matrix
        这个题不是找插入位置而是找数, 返回的是True False, 所以不变量是[lo, hi]?
    解法:
        相比正常binary search就是多了一个array2matrix译码
    """
    s = Solution()
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    matrix= [[1]]
    print(s.searchMatrix(matrix, 16))
