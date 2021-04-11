#
class Solution:
    def backtracking(self,path,nums,start_idx,res):
        
        for i in range(start_idx,len(nums)):
            
            if not path or path[-1] < nums[i]:
                self.backtracking(path+[nums[i]],nums,i+1,res)
        res['length'] = max(res['length'],len(path))
        return 
        
    def lengthOfLIS(self, nums) -> int:
        res = {'length':0}
        self.backtracking([],nums,0,res)
        return res['length']

s = Solution()
# print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(s.lengthOfLIS([0,1,0,3,2,3]))