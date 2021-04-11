#题目：917.仅仅反转字母
#双指针同时靠近，跳过不能反转的字符即可
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        left,right = 0,len(s)-1
        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            elif not s[left].isalpha():
                left += 1
            else:
                right -= 1
        return ''.join(s)