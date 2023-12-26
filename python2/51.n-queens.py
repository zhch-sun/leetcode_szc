#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(idx, used, tmp):  # idx是第i行的情况
            if idx == n:
                tmp1 = [['.'] * n for _ in xrange(n)]  
                for i, j in tmp:
                    tmp1[i][j] = 'Q'  # 一个长str不能直接赋值
                ans.append([''.join(row) for row in tmp1])
                return
            for j in xrange(n):
                cand = set([j, j - idx + 10 * n, j + idx + 100 * n])
                if not cand & used:
                    used |= cand
                    tmp.append((idx, j))
                    dfs(idx + 1, used, tmp)
                    tmp.pop()
                    used -= cand
        used = set()
        ans = []
        dfs(0, used, [])  # set必须传参...
        return ans
if __name__ == '__main__':
    """
    
    """
    s = Solution()
    print(s.solveNQueens(4))
# @lc code=end

