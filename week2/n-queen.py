class Solution:
    def backtracking(self,path,n,r,rc_diff,rc_sum,res):
        if r >= n:
            res.append(path[:])
            return 
        for c in range(n):
            if c not in path and r-c not in rc_diff and r+c not in rc_sum:
                self.backtracking(path+[c],n,r+1,rc_diff+[r-c],rc_sum+[r+c],res)
        return 

    def solveNQueens(self, n: int) -> List[List[str]]:
        path,rc_diff,rc_sum,res = [],[],[],[]
        self.backtracking(path,n,0,rc_diff,rc_sum,res)
        return [['.'*(c)+'Q'+'.'*(n-1-c) for c in p] for p in res]