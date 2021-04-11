#题目:1122.数组的相对排序
#我的解法：由基本暴力解法需要两层循环很容易想到用哈希表来加速查找
class Solution1:
    def relativeSortArray(self, arr1, arr2) :
        mp = {}
        for n in arr1:
            mp[n] = mp.get(n,0) + 1
        res = []
        for n in arr2:
            if n in mp:
                res += [n] * mp.get(n)
                mp.pop(n)
        remain_n = sorted(mp.keys())
        for n in remain_n:
            res += [n] * mp.get(n)
        return res 

#学习一下官方自定义排序的解法
class Solution2:
    def relativeSortArray(self, arr1, arr2) :
        def mycmp(x: int) -> (int, int):
            return (0, rank[x]) if x in rank else (1, x)
        
        rank = {x: i for i, x in enumerate(arr2)}  #这种定义字典的方式还没用过
        arr1.sort(key=mycmp)
        return arr1

#计数排序解法：与哈希表的思想基本相似
class Solution3:
    def relativeSortArray(self, arr1, arr2) :
        upper = max(arr1)
        frequency = [0] * (upper + 1)
        for x in arr1:
            frequency[x] += 1
        
        ans = list()
        for x in arr2:
            ans.extend([x] * frequency[x])
            frequency[x] = 0
        for x in range(upper + 1):
            if frequency[x] > 0:
                ans.extend([x] * frequency[x])
        return ans

import unittest
class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        my_ans = s.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6])
        correct_ans = [2,2,2,1,4,3,3,9,6,7,19]
        self.assertTrue(all(v in correct_ans for v in my_ans) and len(my_ans)==len(correct_ans))

if __name__ == '__main__':
    unittest.main()


