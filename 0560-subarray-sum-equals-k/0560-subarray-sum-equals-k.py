class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s=0
        c=0
        d={}
        for i in nums:
            s+=i
            if s==k:
                c=c+1
            if (s-k) in d:
                c=c+d[s-k]
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return c