#
# @lc app=leetcode id=52 lang=python
#
# [52] N-Queens II
#

# @lc code=start
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 96ms
        def dfs(idx, used):  # idx是第i行的情况
            # 80ms
            if idx == n:
                return 1  # 忘记了..
            ans = 0
            for j in xrange(n):
                cand = set(['c' + str(j), 'a' + str(j - idx), \
                    'b' + str(j + idx)])  # row不可能重复.
                if not cand & used:
                    used |= cand
                    ans += dfs(idx + 1, used)
                    used -= cand
            return ans
        used = set()
        return dfs(0, used)  # set必须传参...

    # def totalNQueens(self, n):
    #     # 64ms
    #     def dfs(idx, used):  # idx是第i行的情况
    #         if idx == n:
    #             return 1  # 忘记了..
    #         ans = 0
    #         for j in xrange(n):
    #             cand = set([j, j - idx + 10 * n, j + idx + 100 * n])
    #             if not cand & used:
    #                 used |= cand
    #                 ans += dfs(idx + 1, used)
    #                 used -= cand
    #         return ans
    #     used = set()
    #     return dfs(0, used)  # set必须传参...

if __name__ == '__main__':
    """
    解法1:
        96ms
        枚举行, 则行不会重复.
        统计列, 以及两条斜线的重复情况. 斜线是y+x=c或者y-x=c
    解法2:
        64ms 想办法把数字放进set里.
        未写: 分成三个set 36ms
        也可以直接用list和x in list. 因为问题小所以更快.
    解法3:
        bit操作, 见最快sub
    """
    s = Solution()
    print(s.totalNQueens(4))
# @lc code=end

