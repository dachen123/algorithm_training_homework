#题目：212.单词搜索II
# 解法：trie树+dfs+回溯
class Solution:
    def _dfs(self,board,i,j,m,n,node,word,res):
        c = board[i][j]
        w = node[c].pop('finish',False)
        if w:          
            res.add(w)
            #return         
        board[i][j] = '@'
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n and board[x][y] in node[c]:
                self._dfs(board,x,y,m,n,node[c],word+c,res)
        board[i][j] = c

    def findWords(self, board, words) :
        if not words:return []
       
        #构建trie
        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char,{})
            node['finish'] = word
        #查询
        res = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    self._dfs(board,i,j,m,n,root,'',res)
        return list(res)

import unittest
class testSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        res = s.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])
        self.assertEqual(len(res),2)
        self.assertTrue('oath' in res)
        self.assertTrue('eat' in res)
if __name__ == '__main__':
    unittest.main()