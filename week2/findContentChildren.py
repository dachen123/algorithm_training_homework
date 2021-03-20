#题目：分发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i,j = len(g)-1,len(s) - 1
        count = 0
        g.sort()
        s.sort()
        while i >= 0 and j >=0 :
            if s[j] >= g[i]:
                count += 1
                i -= 1
                j -= 1
                continue
            i -= 1
        return count