#
# @lc app=leetcode id=864 lang=python
#
# [864] Shortest Path to Get All Keys
#

# @lc code=start
from collections import deque
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        keys = 0
        num_keys = 0
        for i in xrange(M):  # 找起始位置和
            for j in xrange(N):
                if grid[i][j] == '@':
                    startI, startJ = i, j
                elif grid[i][j] in 'abcdef':
                    num_keys += 1

        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        initial = (startI, startJ, 0)
        dq = deque([initial])  # Note szc 都要加[]...
        memo = set([initial])  # Note 都要加[]...
        steps = 0
        while dq:
            for _ in xrange(len(dq)):
                i, j, keys = dq.popleft()
                if grid[i][j] in 'abcdef':
                    keys |= 1 << ord(grid[i][j]) - ord('a')
                    if keys == (1 << num_keys) - 1:
                        return steps

                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] != '#':
                        if grid[ni][nj] in 'ABCDEF' and \
                            not 1 << ord(grid[ni][nj]) - ord('A') & keys:
                            continue
                        state = (ni, nj, keys)
                        if state not in memo:
                            dq.append(state)
                            memo.add(state)
            steps += 1
        return -1

if __name__ == '__main__':
    """
    题设: 找到所有钥匙即可. 身上可以带无穷把钥匙. 
    解法1:
        最短路问题显然BFS. 
        状态设计: 
            keys不能用set. 因为不能hash...
            keys用str则每次修改都要hash..
            keys可以用bit优化
        复杂度: 状态总共有2^k个, m * n * 2 ^ k
    """
    s = Solution()
    print(s.shortestPathAllKeys(["@.a.#",
                                 "###.#",
                                 "b.A.B"]))
    print(s.shortestPathAllKeys(["@..aA","..B#.","....b"]))                                 
# @lc code=end

