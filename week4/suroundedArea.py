#题目：130.被围绕的区域
#并查集解法，效率有点低
class Solution:
    def _parent(self,p,i):
        root = i 
        while p[root] != root: #特殊节点（既边界节点）用-1标记
            root = p[root]
        while p[i] != i:
            x = i 
            i = p[i]
            p[x] = root 
        return root
    def _union(self,p,special_p,i,j):
        p1 = self._parent(p,i)
        p2 = self._parent(p,j)
        p[p2] = p1 
        #这部分必须要加，p1或者p2变为合并集合的root后，要进行标记
        if p1 in special_p or p2 in special_p:
            special_p.add(p1)

    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #最好判断边界
        # if not board:
        #     return 
        m = len(board)
        n = len(board[0])
        p = [i for i in range(m*n)]
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        special_p = set()
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    if (i in (0,m-1) or j in (0,n-1)):
                        #对边界的'O'进行标记
                        special_p.add(self._parent(p,i*n+j))
                    else:
                        #对四联通的节点进行判断
                        for di in range(4):
                            x = i+dx[di]
                            y = j+dy[di]
                            if 0 <= x < m and 0 <= y < n and board[x][y]=='O':
                                self._union(p,special_p,i*n+j,x*n+y)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and self._parent(p,i*n+j) not in special_p:
                    board[i][j] = 'X'
        return 





import unittest
class testSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        matrix = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        s.solve(matrix)
        self.assertEqual(matrix[1][1],'X')
        self.assertEqual(matrix[1][2],'X')
        self.assertEqual(matrix[2][2],'X')

if __name__ == '__main__':
    unittest.main()