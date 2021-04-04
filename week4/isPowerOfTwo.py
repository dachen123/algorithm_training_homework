#题目：231.2的幂

#方法1：消去最低位的1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n-1) == 0 if n!=0 else False

#方法2：获取最低位的1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        return n & -n == n