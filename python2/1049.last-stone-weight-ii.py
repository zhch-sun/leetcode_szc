#
# @lc app=leetcode id=1049 lang=python
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution(object):
    # def lastStoneWeightII(self, stones):
    #     """
    #     :type stones: List[int]
    #     :rtype: int
    #     """
    #     if not stones:
    #         return 0
    #     total = sum(stones)
    #     half = total // 2  # 不能 ceiling div....
    #     f = [False] * (half + 1)
    #     f[0] = True
    #     for n in stones:
    #         for j in xrange(half, n - 1, -1):
    #             f[j] = f[j] | f[j - n]
    #     for i in xrange(half, -1, -1):
    #         if f[i]:
    #             return total - 2 * i

    def lastStoneWeightII(self, stones):
        # 100% 12ms!! 超过所有已经提交的代码
        if not stones:
            return 0
        total = sum(stones)
        half = total // 2  # 不能 ceiling div....
        bits = 1
        for n in stones:
            bits |= bits << n
            if bits & (1 << half):
                return total - 2 * half
        
        for i in xrange(half, -1, -1):
            if bits & (1 << i):
                return total - 2 * i

if __name__ == '__main__':
    """
    题设: 石头两两消除, 问最后一块石头的最小体积
    解法1: 01背包. 
    解法2: 01背包 优化
    """
    s = Solution()
    print(s.lastStoneWeightII([2,7,4,1,8,1]))

# @lc code=end

