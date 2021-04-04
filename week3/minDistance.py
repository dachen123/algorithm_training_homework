#72.编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [[0]*(n+1) for i in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i 
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]+1,dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[m][n]

#空间复杂度优化
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        dp = [0]*(n+1)

        for j in range(n+1):
            dp[j] = j
        tmp = 0
        for i in range(1,m+1):
            for j in range(0,n+1):
                p = dp[j]
                if j==0:
                    dp[j]= i
                elif word1[i-1]==word2[j-1]:
                    dp[j] = min(tmp,dp[j]+1,dp[j-1]+1)
                else:
                    dp[j] = min(tmp+1,dp[j]+1,dp[j-1]+1)
                tmp = p
        return dp[n]

