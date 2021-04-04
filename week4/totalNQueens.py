#52.N皇后II
#解法使用的位运算
#参考文章：https://zhuanlan.zhihu.com/p/22846106
class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def dfs(r,n,col,pie,na):
            if r >= n:
                nonlocal count
                count += 1
                return 
            bits = ((1<<n)-1) & (~(col | pie | na)) #计算可用的列，避免大于n位的数值的干扰，要将高于n位的数消掉
            while bits:
                p = bits & -bits
                bits ^= p   #异或可以让最低位的1消掉
                dfs(r+1,n,col|p,(pie|p)>>1,(na|p)<<1)  #pie与na定义的是撇与捺占据了当前行上的哪些列
        count = 0
        dfs(0,n,0,0,0)
        return count 