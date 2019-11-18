#
# @lc app=leetcode id=1004 lang=python
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        lo = 0
        res = 0
        cnt = 0
        for hi, item in enumerate(A, 1):  # [lo, hi)
            cnt += 1 - item  # 注意这个写法!
            if cnt <= K:
                res = max(res, hi - lo)
            else:
                while cnt > K:
                    cnt -= 1 - A[lo]
                    lo += 1
        return res

    # def longestOnes(self, A, K):
    #     # TLE. 
    #     f = [0] * (K + 2)
    #     ans = 0
    #     for n in A:
    #         for j in xrange(K, -1, -1):  # Note 需要倒序!且取到0...
    #             if n == 1:
    #                 f[j] += 1
    #             elif j == 0:
    #                 f[j] = 0  # 可以通过初始化去掉这个判断
    #             else:
    #                 f[j] = f[j - 1] + 1
    #         ans = max(ans, f[K])
    #     return ans

if __name__ == '__main__':
    """
    题设: 可以翻转k次, 求最大连续1的个数.
    解法1: 
        连续子区间, 滑窗, 每一步找到以hi为结尾的最长序列
    解法2:
        DP TLE
        表示以i为结尾, 最多j个0时最大值
        f[i][j] = f[i-1][j] + 1 or f[i-1][j-1] + 1
        f[j] = f[j] + 1 or f[j-1] + 1
        初始化: 0
        返回值: max所有f[K]
    """
    s = Solution()
    print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
                    
# @lc code=end

