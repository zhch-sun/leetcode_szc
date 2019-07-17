#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:  # 奇怪的特殊情况
            return False
        left = 0
        right = len(matrix) * len(matrix[0]) - 1  # Note overflow
        Col = len(matrix[0])
        while left <= right:  # fake insert pos
            mid = (right - left) // 2 + left
            # quotient, remainder = divmod(mid, Col)
            # item = matrix[quotient][remainder]
            item = matrix[mid//Col][mid%Col]
            if item < target:
                left = mid + 1
            elif item > target:
                right = mid - 1
            else:
                return True
        return False
        # 如果返回的是insert pos, 则不能这样写, 因为有可能超出范围..
        # return True if matrix[left//Col][left%Col] == target else False


if __name__ == '__main__':
    """
    这个题是返回true或者false, 并不简单. 注意不能最后再判断, 因为我的主体找insert位置,
    而这个位置是可能超出select的范围的. 
    正确写法还是
    1. <= 来判断, 确保最后那个位置与target比较. 如果用<号则有可能不比较.
    2. 分三种讨论, 并输出唯一的true
    3. 最后值输出false, 不输出true.
    """
    s = Solution()
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    matrix= [[1]]
    print(s.searchMatrix(matrix, 16))
