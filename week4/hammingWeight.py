#题目：191.位1的个数（汉明重量）
#原来这是 布莱恩克尼根算法。。。，还有一道汉明距离用的相似的解法
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res
