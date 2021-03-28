#打家劫舍版本II
class Solution:
    def _rob(self,nums):
        first,second = 0,0
        for num in nums:
            first,second = second,max(second,first+num)
        return second
    def rob(self, nums) -> int:
        if not nums:
            return 0
        return max(self._rob(nums[1:]),self._rob(nums[:-1])) if len(nums) > 1 else nums[0]



import unittest
class testSolution(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.rob([2,3,2]),3)



if __name__ == '__main__':
    unittest.main()