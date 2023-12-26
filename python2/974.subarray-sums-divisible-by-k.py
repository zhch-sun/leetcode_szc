#
# @lc app=leetcode id=974 lang=python
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        psum, ans = 0, 0
        seen = defaultdict(int)
        seen[0] = 1
        for item in A:
            psum += item
            ans += seen[(psum - K) % K]
            seen[psum % K] += 1  # [0, K-1]
        return ans

if __name__ == '__main__':
    """
    相比560, 只需要mod即可
    """
    s = Solution()
    print(s.subarraysDivByK([4,5,0,-2,-3,1], 5))
        
# @lc code=end

