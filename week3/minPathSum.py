#最小路径和
#空间复杂度为n^2
class Solution1:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*(n) for i in range(m)]  #dp[i][j]表示从(0,0)到(i,j)的最小路径
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):                
                dp[i][j] = min(dp[i][j-1],dp[i-1][j]) + grid[i][j]
               
        return dp[m-1][n-1] 

#空间复杂度优化
class Solution2:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]

        for j in range(1,n):
            dp[j] = dp[j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    dp[j] +=  grid[i][0]   
                else:             
                    dp[j] = min(dp[j],dp[j-1]) + grid[i][j]
               
        return dp[n-1] 


import unittest
class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        self.assertEqual(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]),7)
    def test_solution2(self):
        s = Solution2()
        self.assertEqual(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]),7)


if __name__ == '__main__':
    unittest.main()


