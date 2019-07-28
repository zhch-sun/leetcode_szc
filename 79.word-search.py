#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#
class Solution(object):
    # def exist(self, board, word):
    #     """
    #     :type board: List[List[str]]
    #     :type word: str
    #     :rtype: bool
    #     """
    #     def dfs(i, j, k, tmp):
    #         # check current
    #         if board[i][j] != word[k]:
    #             return False
    #         if k + 1 == len(word):  # note k + 1
    #             return True      
    #         # generate next          
    #         tmp.append((i, j))
    #         dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    #         for d in dirs:
    #             ti = i + d[0]
    #             tj = j + d[1]
    #             if 0 <= ti < m and 0 <= tj < n and (ti, tj) not in tmp:  # 这个判断条件不简单
    #                 if dfs(ti, tj, k + 1, tmp):
    #                     return True
    #         tmp.pop()
    #         return False
        
    #     # if not word:
    #     #     return True
    #     # if not board:
    #     #     return False
    #     m, n = len(board), len(board[0])
    #     for i in range(m):
    #         for j in range(n):
    #             # 不能写下面的写法... 因为这样写board[i][j]没有放到tmp中
    #             if dfs(i, j, 0, []):  # board[i][j] == word[0] and 
    #                 return True
    #     return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k, tmp):
            # check current
            if board[i][j] != word[k]:
                return False
            if k + 1 == len(word):  # note k + 1
                return True      
            # generate next     
            tmp.add((i,j))     
            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for d in dirs:
                ti = i + d[0]
                tj = j + d[1]
                if 0 <= ti < m and 0 <= tj < n and (ti, tj) not in tmp:  # 这个判断条件不简单
                    if dfs(ti, tj, k + 1, tmp):
                        return True
            tmp.remove((i,j))
            return False
    
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # 不能写下面的写法... 因为这样写board[i][j]没有放到tmp中
                if dfs(i, j, 0, set()):  # board[i][j] == word[0] and 
                    return True
        return False    
        
    # def exist(self, board, word):
    #     def dfs(i, j, k):
    #         if board[i][j] != word[k]:
    #             return False
    #         if k == len(word) - 1:  # note k + 1
    #             return True      

    #         save, board[i][j] = board[i][j], '#'
    #         dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    #         for d in dirs:
    #             ti = i + d[0]
    #             tj = j + d[1]
    #             if 0 <= ti < m and 0 <= tj < n and dfs(ti, tj, k + 1):
    #                 return True
    #         board[i][j] = save
    #         return False
        
    #     m, n = len(board), len(board[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if dfs(i, j, 0):
    #                 return True
    #     return False

    # def exist(self, board, word):
    #     def dfs(i, j, k):
    #         if k == len(word):
    #             return True      

    #         save, board[i][j] = board[i][j], '#'
    #         dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    #         for d in dirs:
    #             ti = i + d[0]
    #             tj = j + d[1]
    #             if 0 <= ti < m and 0 <= tj < n and board[ti][tj] == word[k] and \
    #                 dfs(ti, tj, k + 1):  # 真难呀, 一个是k 一个是k+1
    #                 return True
    #         board[i][j] = save
    #         return False
        
    #     m, n = len(board), len(board[0])
    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == word[0] and dfs(i, j, 1):
    #                 return True
    #     return False        

if __name__ == '__main__':
    """
    解法1: for循环+backtrack. 用list存着之前走过的路径, 但是有若干细节需要注意. 
    解法2: 和上面同样的思路, 用set存着, 这样查找速度为O(1). 加速了很多! 
    解法3: 走过的路赋值为奇怪的东西, 这样其实用同样大小的memory. 速度一样
    这个解法2因为在中间跳出, 会改变board的值....
    解法4: 因为调用了更少的函数所以更快, 但是条件太tricky了. 还是解法1把.
    """
    s = Solution()
    board = \
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    print(s.exist(board, "ABCCED"))
    # print(s.exist(board, "SEE"))
    # print(s.exist(board, "ABCB"))

    # board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
    # print(s.exist(board, "aaaaaaaaaaab"))

    # board = [["a","a"]]
    # print(s.exist(board, "aaa"))


