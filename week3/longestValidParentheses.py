#题目：最长有效括号
#最先想到暴力法，时间复杂度O(n^3)，空间复杂度O(n)，提交超时
class Solution1:
    def _is_valid(self,s):
        st = []
        for c in s:
            if c == '(':
                st.append(c)
            else:
                if st and st[-1]=='(':
                    st.pop()
                else:
                    return False
        if not st:
            return True
        else:
            return False

    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        for j in range(len(s)):
            for i in range(j):
                if self._is_valid(s[i:j+1]):  #判读s[i..j]是否为有效括号
                    ans = max(ans,len(s[i:j+1]))
        return ans

#动态规划法：状态方程比较难想，还要考虑异常边界处理
class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        dp = [0] * len(s) #以i结尾的有效子串
        for i in range(1,len(s)):
            if s[i] == ')':
                if s[i-1]=='(':
                    dp[i] = dp[i-2] + 2 if i >=2 else 2
                #elif s[i-1]==')' and s[i-dp[i-1]-1]=='(':
                elif i-dp[i-1] > 0 and s[i-dp[i-1]-1]=='(': #要确保i-dp[i-1]的索引存在，否则计算出错
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2] if i>=2 else 0
                ans = max(ans,dp[i])
                 
        return ans

#栈匹配的方式
#官方没有说清楚的是，保留栈底为最近一个无法匹配的右括号，还有一个目的：使得i-栈顶元素值刚好为有效串长度，否则要加一
class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        st = [-1]
        for i,c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans = max(i-st[-1],ans)                
        return ans

#计数器方式：
class Solution4:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        left,right = 0,0
        for c in s:
            if c=='(':
                left += 1
            else:
                right += 1
            if left==right:
                ans = max(ans,left *2)
            elif right > left: #认为当前字符为无效字符，丢弃不纳入计数
                left,right = 0,0
        left,right = 0,0
        for c in s[::-1]:
            if c=='(':
                left += 1
            else:
                right += 1
            if left==right:
                ans = max(ans,left*2)
            elif left > right:
                left,right = 0,0                
        return ans


import unittest
class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        self.assertEqual(s.longestValidParentheses("(()"),2)
        self.assertEqual(s.longestValidParentheses(")()())"),4)
        self.assertEqual(s.longestValidParentheses(""),0)

    def test_solution2(self):
        s = Solution2()
        self.assertEqual(s.longestValidParentheses("(()"),2)
        self.assertEqual(s.longestValidParentheses(")()())"),4)
        self.assertEqual(s.longestValidParentheses(""),0)

    def test_solution3(self):
        s = Solution3()
        self.assertEqual(s.longestValidParentheses("(()"),2)
        self.assertEqual(s.longestValidParentheses(")()())"),4)
        self.assertEqual(s.longestValidParentheses(""),0)

    def test_solution4(self):
        s = Solution4()
        self.assertEqual(s.longestValidParentheses("(()"),2)
        self.assertEqual(s.longestValidParentheses(")()())"),4)
        self.assertEqual(s.longestValidParentheses(""),0)


if __name__ == '__main__':
    unittest.main()
