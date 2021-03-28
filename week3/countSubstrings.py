#题目：回文子串
#动态规划法
#这里的遍历方式比较巧妙，要注意两个点：
#1.根据dp[i][j]定义：s[i][j]是否为回文串，则i必定小于等于j
#2.要求dp[i][j]，dp[i+1][j-1]需要提前求出，这里按列优先方式填值
class Solution1:
    def countSubstrings(self, s: str) -> int:
        dp = [[0]*len(s) for i in range(len(s))]
        res = 0
        for j in range(len(s)):
            for i in range(j+1):
                if s[i]==s[j] and ( j-i<2 or dp[i+1][j-1] ):
                    dp[i][j] = True
                    res += 1
        return res

#中心拓展法
#官方定义中心优点啰嗦，实际上字符串的中心位置为字符个数(n)加上字符间隙(n-1)，因此为2n-1
class Solution2:
    def countSubstrings(self, s: str) -> int:
        res = 0
        s_size = len(s)
        for i in range(2*s_size-1):
            l,r = i//2,i//2 + i%2
            while l>=0 and r<s_size and s[l]==s[r]:
                res +=1
                l -= 1
                r += 1
        return res

#马拉车算法(最优解)
class Solution3:
    def countSubstrings(self, s) -> int:
        new_s = '^#'
        for c in s:
            new_s = new_s + c + '#'
        new_s += '$'
        new_s_size = len(new_s)
        p = [0] * new_s_size
        iMax,rMax,res = 0,0,0
        for i in range(2,new_s_size-2):  #原版是1..new_s_size-1,但测试发现开头和结尾的两个'#'可以不用进入循环
            i_mirror = 2 *iMax - i
            if i <= rMax:
                p[i] = min(rMax-i,p[i_mirror])
            else:
                p[i] = 0  #官方版本是初始化为1,取子串用的是左闭右开的方式，我这里用0，取左闭右闭的方式
            while new_s[i+p[i]+1] == new_s[i-p[i]-1]:
                p[i] += 1
            if i+p[i] > rMax:
                rMax = i + p[i]
                iMax = i 
            res += (p[i]+1) // 2 #取p[i]/2向上取整，所以先加一，这里很巧妙，p[i]为奇数时，中心字符必为原字符串字符，为偶数时必为'#'字符，为了考虑奇数情况要把中心字符考虑进去，所以向上取整
        return res 


import unittest
class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        self.assertEqual(s.countSubstrings("abc"),3)
    def test_solution2(self):
        s = Solution2()
        self.assertEqual(s.countSubstrings("abc"),3)
    def test_solution3(self):
        s = Solution3()
        self.assertEqual(s.countSubstrings("abc"),3)

if __name__ == '__main__':
    unittest.main()


