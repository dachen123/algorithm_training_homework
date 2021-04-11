#541.反转字符串II
#我的解法：直接模拟，比较考验下标指针的移动
class Solution1:
    def reverseStr(self, s: str, k: int) -> str:
        if k <= 1:return s 
        i = 0
        s = list(s)
        while i+2*k-1 < len(s):
            for j in range(k//2):
                s[i+j],s[i+k-1-j] = s[i+k-1-j],s[i+j]
            i += 2*k
        if i + k - 1 < len(s): #剩余字符大于等于k小于2k的情况
            for j in range(k//2):
                s[i+j],s[i+k-1-j] = s[i+k-1-j],s[i+j]
        else: #剩余字符小于k的情况
            j = len(s)-1
            while i < j:
                s[i],s[j] = s[j],s[i]
                i += 1 #不要忘记指针移动
                j -= 1
        return ''.join(s)

#官方解法：比较简洁牛逼
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k <= 1:return s    
        s = list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)

import unittest

class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        self.assertEqual(s.reverseStr("abcdefg",2),"bacdfeg")
    
if __name__ == '__main__':
    unittest.main()