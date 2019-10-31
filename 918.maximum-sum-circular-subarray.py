#
# @lc app=leetcode id=918 lang=python
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from collections import deque
class Solution(object):
    # def maxSubarraySumCircular(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     N = len(A)
    #     P = [0] * (2 * N + 1)
    #     for i in xrange(2 * N):
    #         P[i + 1] = P[i] + A[i % N]
        
    #     dq = deque()  # 初始化呀..
    #     ans = float('-inf')
    #     for j, item in enumerate(P):
    #         if dq and dq[0] < j - N:
    #             dq.popleft()
    #         if dq:
    #             ans = max(ans, item - P[dq[0]])
    #         while dq and item <= P[dq[-1]]:
    #             dq.pop()
    #         dq.append(j)
    #     return ans

    def maxSubarraySumCircular(self, A):
        N = len(A)
        P = [0] * (2 * N + 1)
        for i in xrange(2 * N):
            P[i + 1] = P[i] + A[i % N]
        
        dq = deque([0])  # 初始化呀..
        ans = float('-inf')
        for j in range(1, len(P)):
            item = P[j]
            if dq[0] < j - N:
                dq.popleft()
            ans = max(ans, item - P[dq[0]])
            while dq and item <= P[dq[-1]]:
                dq.pop()
            dq.append(j)
        return ans

if __name__ == '__main__':
    """
    解法1: 
        对于i, j pair, 对于固定的j, 我们希望Pi尽可能小且
        j - N <= i <= j (注意这是有范围的!)
        如果对于i1 < i2 且 Pi1 > Pi2, 则i1不需要考虑. 
        即越近的P要越小
        TODO 貌似dq初始化可以保证dq一直有值避免很多判断. 
    解法2:
        TODO 53题是正常数组的.. 用的DP
    """
    s = Solution()
    print(s.maxSubarraySumCircular([1,-2,3,-2]))      
    print(s.maxSubarraySumCircular([5,-3,5]))      
    print(s.maxSubarraySumCircular([3,-1,2,-1]))      
    print(s.maxSubarraySumCircular([3,-2,2,-3]))      
    print(s.maxSubarraySumCircular([-2,-3,-1]))      
# @lc code=end

