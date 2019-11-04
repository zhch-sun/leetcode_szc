#
# @lc app=leetcode id=918 lang=python
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
from collections import deque
class Solution(object):
    # def maxSubarraySumCircular(self, A):
    #     N = len(A)
    #     P = [0] * (2 * N + 1)
    #     for i in xrange(2 * N):
    #         P[i + 1] = P[i] + A[i % N]
        
    #     ans = float('-inf')
    #     dq = deque([0])  # Note 必须初始化, 递增序列
    #     for i in xrange(1, len(P)):  # Note 必须从1开始
    #         n = P[i]
    #         if dq and i - dq[0] > N:  # Note 没有=...
    #             dq.popleft()
    #         ans = max(ans, n - P[dq[0]])  # Note 必须在这里赋值
    #         while dq and n <= P[dq[-1]]:
    #             dq.pop()
    #         dq.append(i)
    #     return ans

    def maxSubarraySumCircular(self, A):
        def kadane(A, lo, hi):
            localV = globalV = float('-inf')
            for i in xrange(lo, hi + 1):
                n = A[i]
                localV = n + max(0, localV)
                globalV = max(globalV, localV)
            return globalV
        S = sum(A)
        Aminus = [-n for n in A]  # 注意不能 ~n, 这里不仅需要比较还需要值.
        N = len(A)
        ans1 = kadane(A, 0, N - 1)
        ans2 = kadane(Aminus, 0, N - 2)
        ans3 = kadane(Aminus, 1, N - 1) 
        return max(ans1, S + ans2, S + ans3)

if __name__ == '__main__':
    """
    解法1: 
        对于i, j pair, 对于固定的j, 我们希望Pi尽可能小且
        j - N <= i <= j (注意这是有范围的!)
        如果对于i1 < i2 且 Pi1 > Pi2, 则i1不需要考虑. 
        即越近的P要越大, 因为可能在未来用到. 如果又近又小, 那前面的就没意义了
        Note只能dq初始化, 避免P[0]给answer赋值, 循环从1开始
    解法2:
        53题是正常数组的最大子序列和 kadane算法. 
        这个题是分三种情况讨论:
            1. 如果最后解在中间, 正常kadane即可
            2. 如果解再两端, 则解是S-kadane, kadane找最小值即可
                然而解可能是找到全体, 即两端为空.. 所以:
                2.1 找[0:N-2]
                2.2 找[1,N-1]
    解法3: 不管
        仍有更快的解法. 计算左右sum? 
    """
    s = Solution()
    print(s.maxSubarraySumCircular([-2,-3,-2]))      
    print(s.maxSubarraySumCircular([1,-2,3,-2]))      
    print(s.maxSubarraySumCircular([3,1,3,2,6]))      
    # print(s.maxSubarraySumCircular([5,-3,5]))      
    # print(s.maxSubarraySumCircular([3,-1,2,-1]))      
    # print(s.maxSubarraySumCircular([3,-2,2,-3]))      
    # print(s.maxSubarraySumCircular([-2,-3,-1]))      
# @lc code=end

