#题目：547.省份数量
#并查集解法
class Solution:
    def _parent(self,p,i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i 
            p[x] = root 
            i = p[i]
        return root

    def _union(self,p,i,j):
        p1 = self._parent(p,i)
        p2 = self._parent(p,j)
        p[p2] = p1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:return 0
        n = len(isConnected)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    self._union(p,i,j)
        
        return len([i for i in range(len(p)) if p[i]==i])