#题目：680.验证回文字符串II
class Solution:
    def checkPalindrome(self,s):
        left,right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False 
            left += 1
            right -= 1
        return True 
    
    def validPalindrome(self, s: str) -> bool:
        skip_flag = False
        left,right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                return self.checkPalindrome(s[left+1:right+1]) or self.checkPalindrome(s[left:right])  #可能删除左指针或右指针上的字符
            left += 1
            right -= 1 
        return True

import unittest
class testSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertTrue(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
        
       

if __name__ == '__main__':
    unittest.main()