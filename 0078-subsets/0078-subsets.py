class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[]
        for i in range(2**len(nums)):
            l=[]
            for j in range(len(nums)):
                if i >> j & 1:
                    l.append(nums[j])
            a.append(l)
        return a
                    
            