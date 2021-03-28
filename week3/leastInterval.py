#题目：任务调度器
#最容易理解的解法
class Solution1:
    def leastInterval(self, tasks, n) -> int:
        import collections
        freq = collections.Counter(tasks)
        m = len(freq.keys())
        nextValid = [1] * m
        rest = list(freq.values())
        time = 0
        for i in range(len(tasks)):
            time += 1
            minNextValid = min([nextValid[i] for i in range(m) if rest[i] > 0])
            time = max(time,minNextValid)

            best = -1
            for j in range(m):
                if rest[j] and nextValid[j] <= time:
                    if best==-1 or rest[j] > rest[best]:
                        best = j
            nextValid[best] = time + n + 1
            rest[best] -= 1
        return time


#官方构造方法
class Solution2:
    def leastInterval(self, tasks, n) -> int:
        import collections
        freq = collections.Counter(tasks)
        maxExec = max(freq.values())
        maxExecCount = len([v for v in freq.values() if v==maxExec])
        return max((maxExec-1)*(n+1)+maxExecCount,len(tasks))


import unittest
class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        self.assertEqual(s.leastInterval(["A","A","A","B","B","B"],2),8)
    
    def test_solution2(self):
        s = Solution2()
        self.assertEqual(s.leastInterval(["A","A","A","B","B","B"],2),8)


if __name__ == '__main__':
    unittest.main()
