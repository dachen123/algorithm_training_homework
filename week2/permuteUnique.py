#题目：全排列II
class Solution:
    def backtracking(self,path,nums,used,res):
        if len(path)==len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]= True
                self.backtracking(path+[nums[i]],nums,used,res)
                used[i]=False
        return  
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False for i in range(len(nums))]
        path,res = [],[]
        nums.sort()
        self.backtracking(path,nums,used,res)
        return res