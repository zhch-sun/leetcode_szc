#
# @lc app=leetcode id=1000 lang=python
#
# [1000] Minimum Cost to Merge Stones
#

# @lc code=start
class Solution(object):
    # def mergeStones(self, stones, K):
    #     """
    #     :type stones: List[int]
    #     :type K: int
    #     :rtype: int
    #     """
    #     # 错解...
    #     N = len(stones)
    #     if N == 1:
    #         return 0
    #     if (N - K) % (K - 1) != 0:
    #         return -1
    #     f = [[0] * N for _ in xrange(N)]
    #     for j in xrange(K - 1, N):
    #         for i in xrange(j - K + 1, -1, -1):
    #             ans = float('inf')
    #             for v in xrange(j - K + 1, i - 1, -1):
    #                 cur = sum(stones[v: v + K])
    #                 if v - 1 > i:
    #                     cur += f[i][v - 1]
    #                 if j > v + K:
    #                     cur += f[v + K][j]
    #                 ans = min(ans, cur)
    #             f[i][j] = ans
    #     return f[0][N-1]

    def mergeStones(self, stones, K):
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        def dp(i, j):
            if (i, j) in f:
                return f[i, j]
            if j - i + 1 < K: return 0
            res = min(dp(i, mid) + dp(mid + 1, j) for mid in range(i, j, K - 1))
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            f[i, j] = res
            return res
        f = {}
        return dp(0, n - 1)


if __name__ == '__main__':
    """
    TODO: 没有理解, 也不想搞
    解法:
        整除性质推导:  
            N = k + (k - 1) * i
            N - k mod k - 1 
        区间和应该搞prefix sum...
    区间DP:
        错误状态转移:
            先sum [m: m+K]的区间导致最优
            f[i][j] = min(sum(nums[m:m+K])+f[i][k-1]+f[k+3][j])
            复杂度很高.
        正确状态转移:
            每个m把ij分成两块, 先处理左边, 再处理右边.
            这样m值有N/k个有效位置, 比错解快很多.
            最终再merge到一起
        初始化: 0?
        返回值: f[0][N-1]
    """
    s = Solution()
    print(s.mergeStones([3,2,4,1], 2))
    print(s.mergeStones([3,2,4,1], 3))
    print(s.mergeStones([3,5,1,2,6], 3))
# @lc code=end

