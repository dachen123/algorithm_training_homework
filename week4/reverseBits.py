#题目：190.颠倒二进制位
# 循环颠倒
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res |= (n & 1) << (31 - i)
            n >>= 1
        return res

#分治，优点tricky，可以学一下分治的思想
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        # M1 = 0x55555555 # 01010101010101010101010101010101
        # M2 = 0x33333333 # 00110011001100110011001100110011
        # M4 = 0x0f0f0f0f # 00001111000011110000111100001111
        # M8 = 0x00ff00ff # 00000000111111110000000011111111
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)

        return n