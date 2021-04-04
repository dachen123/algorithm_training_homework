#题目：青蛙过河
#最先想到的暴力方法：尝试所有可能的走法，如果有一条走法能到达终点石头，则青蛙能过河
#利用回溯尝试当前石头能跳到的石头，最终超时
class Solution:
    def backtracking(self,stones,pos,start_idx,k,res):
        if start_idx >= len(stones)-1:
            res['result'] = True
            return 
        for p in pos:
            for i in range(start_idx+1,len(stones)):
                dis = stones[start_idx] + k + p
                if dis < stones[i]:
                    break
                elif dis==stones[i]:
                    self.backtracking(stones,pos,i,k+p,res)

    def canCross(self, stones: List[int]) -> bool:
        res = {'result':False}
        self.backtracking(stones,[-1,0,1],0,0,res)
        return res['result']