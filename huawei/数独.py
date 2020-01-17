def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    def dfs(memo, i, j): 
        if j == 9:
            i += 1
            j = 0  # 没有return
        if i == 9:  # 这个必须在下面.. 并且没有and j==9
            return True
        if board[i][j] != 0:
            return dfs(memo, i, j + 1)
        for n in xrange(1, 10):
            cand = set([(i // 3 , j // 3, n), (i + 10, n), \
                (j + 100, n)])
            if not memo & cand:
                memo |= cand  # Note 一开始写成cand |= memo....
                board[i][j] = str(n)
                if dfs(memo, i, j + 1):
                    return True
                board[i][j] = 0
                memo -= cand
        return False

    memo = set()  # 预先初始化
    for i in xrange(9):
        for j in xrange(9):
            if board[i][j] != 0:
                n = int(board[i][j])  # n 必须是0-based.. 
                memo |= set([(i // 3 , j // 3, n), (i + 10, n), \
                    (j + 100, n)])  # 前面的左边是0-based
    dfs(memo, 0, 0)
    return board

while True:
    try:
        board = []
        for i in range(9):
            board.append(map(int,raw_input().split()))
        solveSudoku(board)
        for i in range(9):
            print(' '.join(board[i]))
    except:
        break
            