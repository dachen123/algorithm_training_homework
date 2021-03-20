#扫雷游戏，判格子合法做的不太好
class Solution:
    def _dfs(self,board,r,c,rows,cols):
        
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c]=='M' or board[r][c]!='E':
            return 
        #看周围是否有雷
        count = 0
        if r < rows -1 and board[r+1][c]=='M': 
            count += 1
        if c < cols-1 and board[r][c+1]=='M': 
            count += 1
        if r < rows-1 and c < cols-1 and board[r+1][c+1]=='M':
            count += 1
        if r > 0 and board[r-1][c]=='M':
            count += 1
        if r > 0 and c < cols-1 and board[r-1][c+1]=='M':
            count += 1
        if c > 0 and board[r][c-1]=='M':
            count += 1
        if r < rows-1 and c > 0 and board[r+1][c-1]=='M':
            count += 1
        if r > 0 and c > 0 and board[r-1][c-1] == 'M':
            count += 1
        if count > 0:
            board[r][c] = '%s' % count
            return 
        else:
            board[r][c] = 'B'
        if r < rows-1:
            self._dfs(board,r+1,c,rows,cols)
        if c < cols -1:
            self._dfs(board,r,c+1,rows,cols)
        if r < rows-1 and c < cols-1:
            self._dfs(board,r+1,c+1,rows,cols)
        if r > 0:
            self._dfs(board,r-1,c,rows,cols)
        if r > 0 and c < cols-1:
            self._dfs(board,r-1,c+1,rows,cols)
        if c > 0:
            self._dfs(board,r,c-1,rows,cols)
        if r < rows-1 and c > 0:
            self._dfs(board,r+1,c-1,rows,cols)
        if r > 0 and c > 0:
            self._dfs(board,r-1,c-1,rows,cols)
        return 
    def updateBoard(self, board, click) :
        rows = len(board)
        cols = len(board[0])
        r,c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        self._dfs(board,r,c,rows,cols)
        return board
                
