#题目：322.零钱兑换
#傻递归，超时
class Solution:
    def coinSelect(self,coins,path,amount,res):
        if amount==0:
            res['num'] = min(res['num'],len(path))
        for c in coins:
            if amount - c >=0:
                self.coinSelect(coins,path+[c],amount-c,res)

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = {'num':float('inf')}
        self.coinSelect(coins,[],amount,res)
        return -1 if res['num']==float('inf') else res['num']

#常规动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1

#tricky动态规划
#巧妙的地方：1.i从coin开始遍历，保证i-coin >=0
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1



