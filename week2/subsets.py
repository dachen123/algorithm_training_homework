#题目：子集
class Solution:
    def _dfs(self,path,nums,start_idx,res):
        res.append(path[:])
        if start_idx > len(nums):
            return 
        for i in range(start_idx,len(nums)):
            self._dfs(path+[nums[i]],nums,i+1,res)
        return 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path,res = [],[]
        self._dfs(path,nums,0,res)
        return res