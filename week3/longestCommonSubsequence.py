#题目：最长公共子序列
#动态转移方程本身比较好想，关建是纠结了半天：为什么text1[i] 和text2[j]相等时，最优解是dp[i-1][j-1]+1，
#而不可能是dp[i-1][j]和dp[i][j-1]中的一个，这里是自己钻牛角尖了，本身dp[i][j]的定义就是最长子序列的长度
#，毫无疑问dp[i-1][j]和dp[i][j-1] 都不可能大于dp[i-1][j-1] + 1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

import unittest
class testSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.longestCommonSubsequence("abcde","ace"),3)

if __name__ == '__main__':
    unittest.main()
