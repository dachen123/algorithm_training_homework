#题目：242.有效的字母异位词
#字母计数的方式
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_table = [0] * 26
        for c in s:
            letters_table[ord(c)-ord('a')] += 1
        for c in t:
            cidx = ord(c)-ord('a')
            letters_table[cidx] -= 1
            if letters_table[cidx] < 0:
                return False 
        return all(x==0 for x in letters_table)

#排序的方式
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s = sorted(s)
        t = sorted(t)
        return ''.join(s) == ''.join(t)

import unittest
class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        self.assertTrue(s.isAnagram('anagram','nagaram'))

    def test_solution2(self):
        s = Solution2()
        self.assertTrue(s.isAnagram('anagram','nagaram'))

if __name__ == '__main__':
    unittest.main()
