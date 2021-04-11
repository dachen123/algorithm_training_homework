#题目：151.翻转字符串里的单词
#库函数搞定版本
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.strip().split()))

#用索引下标手动模拟版本
class Solution:
    def strip_spaces(self,s):
        left,right = 0,len(s)-1
        while left<=right and s[left]==' ':
            left += 1
        while left<=right and s[right]==' ':
            right -= 1
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        return output

    def reverse(self,s,start,end):
        left,right = start,end
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1

    def reverse_each_word(self,s):
        start,end = 0,0
        while start < len(s):
            while end < len(s) and s[end] != ' ': #时刻预防数组越界
                end += 1
            self.reverse(s,start,end-1)
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        s = self.strip_spaces(s)
        self.reverse(s,0,len(s)-1)
        self.reverse_each_word(s)
        return ''.join(s)
