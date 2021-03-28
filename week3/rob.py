#题目：打家劫舍
#二维数组实现法
class Solution1:
    def rob(self, nums) -> int:
        dp = [[0]*2 for i in range(len(nums))] #二维数组,0表示不偷，1表示偷
        dp[0][0],dp[0][1] = 0,nums[0]
        for i in range(1,len(nums)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[len(nums)-1][0],dp[len(nums)-1][1])
#一维数组
class Solution2:
    def rob(self, nums) -> int:
        dp = [0]*(len(nums)+1) #一维数组，索引0..len(nums)表示要偷的房子数目，dp[i]表示偷i间房子的最大价值
        dp[1] = nums[0]
        for i in range(2,len(nums)+1):
            dp[i]= max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[-1]

#常量空间优化，关于first和second的初始化，只有都为0的情况下能满足遍历nums数组每个元素，
#状态方程都不会出错，其实也可以second初始化为nums[0]，然后遍历从1号元素开始
class Solution3:
    def rob(self, nums) -> int:
        first,second = 0,0 #常量空间优化
        for num in nums:
            first,second = second,max(second,first+num)
        return second


import unittest
class testSolution(unittest.TestCase):
    def test_solution1(self):
        s = Solution1()
        self.assertEqual(s.rob([1,2,3,1]),4)

    def test_solution2(self):
        s = Solution2()
        self.assertEqual(s.rob([1,2,3,1]),4)

if __name__ == '__main__':
    unittest.main()