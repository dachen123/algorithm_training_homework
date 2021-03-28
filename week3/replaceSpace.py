class Solution:
    def replaceSpace(self, s) -> str:
        count = 0
        s_list = list(s)
        for c in s_list:
            if c==' ':  #注意判断不要犯错，空格不是空串
                count += 1
        s_list = s_list + ['' for i in range(count*2)] #生成等于新字符串长度的字符list
        i,j = len(s_list)-1,len(s) -1
        while i >=0 and j >=0:
            if s_list[j] != ' ':  #原字符不是空格的，直接拷贝到list中正确的位置上
                s_list[i] = s_list[j]
            else:  #空格用题意要求的字符代替
                s_list[i] = '0'
                s_list[i-1] = '2'
                s_list[i-2] = '%'
                i -= 2
            i -= 1
            j -= 1
        return ''.join(s_list)

import unittest
class testSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.replaceSpace("We are happy."),"We%20are%20happy.")

if __name__ == '__main__':
    unittest.main()