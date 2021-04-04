#题目：200.岛屿数量
#并查集解法
class Solution:
    def _parent(self,p,i):
        root = i 
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i 
            i = p[i]
            p[x] = root 
        return root

    def _union(self,p,p_set,i,j):
        p1 = self._parent(p,i)
        p2 = self._parent(p,j)
        p[p2] = p1
        if p2 in p_set:
            p_set.remove(p2)
        p_set.add(p1)
        
    def numIslands(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        #count = 0
        p = [i for i in range(rows*cols)]
        p_set = set()
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    p_set.add(self._parent(p,i*cols+j))
                    import pdb;pdb.set_trace()
                    for di in range(4):
                        x = i + dx[di]
                        y = j + dy[di]
                        if 0 <= x < rows and 0 <= y < cols and grid[i][j] == '1':
                            self._union(p,p_set,i*cols+j,x*cols+y)
        print(p_set)
        return len(p_set)


import unittest
class testSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        print(s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

if __name__ == '__main__':
    unittest.main()