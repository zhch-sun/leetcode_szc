#
# @lc app=leetcode id=862 lang=python
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """


if __name__ == '__main__':
    """
    题设: 
        返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
        如果没有和至少为 K 的非空子数组，返回 -1
        1 <= A.length.  -10 ^ 5 <= A[i] <= 10 ^ 5
    """
    s = Solution()
    print(s.shortestSubarray([1], 1))     
    print(s.shortestSubarray([1,2], 4))     
    print(s.shortestSubarray([2,-1,2], 4))     
# @lc code=end

