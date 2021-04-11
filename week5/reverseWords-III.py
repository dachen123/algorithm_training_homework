#题目：557.反转字符串中的单词III
class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        start,end = 0,0
        while start < len(s):
            while end < len(s) and s[end] != ' ':
                end += 1
            s[start:end] = reversed(s[start:end])
            end += 1
            start = end 
        return ''.join(s)