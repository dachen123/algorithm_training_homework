#题目：387.字符串中的第一个唯一字符
#没什么好说的，用哈希表记录频次即可
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for c in s:
            mp[c] = mp.get(c,0) + 1
        for idx,c in enumerate(s):
            if mp[c]==1:
                return idx 
        return -1
