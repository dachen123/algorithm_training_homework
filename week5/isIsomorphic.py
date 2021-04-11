#题目：205.同构字符串
#我的解法，必须同时保证正向映射和反向映射都通过,用哈希表保存映射关系
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = t[i]
            else:
                if t[i] != mp[s[i]]:
                    return False
        re_mp = {}
        for i in range(len(t)):
            if t[i] not in re_mp:
                re_mp[t[i]] = s[i]
            else:
                if s[i] != re_mp[t[i]]:
                    return False
        return True

