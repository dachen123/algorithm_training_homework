# O(n)空间复杂度解法，一开始过于情况讨论的不对，情况总结如下：
# 1. 当前字符为'0'时，前面字符只有'1'和'2'的时候才有能解码的可能，其他字符均无解；
# 2. 当前字符为任意除'0'字符情况下，当前字符和之前字符要在11~26之间才能有两种拆分方法
# 3.其他情况当前字符拆法与前一字符拆法相同
class Solution1:
    def numDecodings(self, s) -> int:
        if not s:
            return 0
        s_len = len(s)    
        dp = [0] * (s_len+1)
        if s[0] == '0':
            return 0
        if s_len == 1:
            return 1
        dp[1],dp[0] = 1,1


        for i in range(2,s_len+1):
            if s[i-1]=='0':
                if (s[i-2]=='1' or s[i-2]=='2'):
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-2]=='1':
                dp[i] = dp[i-1] + dp[i-2]
            elif s[i-2]=='2' and s[i-1] in ('1','2','3','4','5','6'):
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[s_len]

#上面解法有两个判断过于冗余，可以合二为一
class Solution2:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        s_len = len(s)    
        dp = [0] * (s_len+1)
        if s[0] == '0':
            return 0
        if s_len == 1:
            return 1
        dp[1],dp[0] = 1,1
        special_code = [str(i) for i in range(11,27)]

        for i in range(2,s_len+1):
            if s[i-1]=='0':
                if (s[i-2]=='1' or s[i-2]=='2'):
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-2:i] in special_code:              
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        return dp[s_len]

#空间复杂度优化
class Solution3:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        s_len = len(s)    
        if s[0] == '0':
            return 0
        if s_len == 1:
            return 1
        first,second = 1,1
        special_code = [str(i) for i in range(11,27)]
        for i in range(1,s_len):
            if s[i]=='0':
                if (s[i-1]=='1' or s[i-1]=='2'):
                    third = first
                else:
                    return 0
            elif s[i-1:i+1] in special_code:              
                third = first + second
            else:
                third = second
            first = second
            second = third

        return second

  
import unittest
class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        self.assertEqual(s.numDecodings("12"),2)
    def test_solution2(self):
        s = Solution2()
        self.assertEqual(s.numDecodings("12"),2)


if __name__ == '__main__':
    unittest.main()      