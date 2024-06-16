class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s=0
        d={}
        c=0
        for i in nums:
            s=s+i
            r=s%k
            if r not in d:
                d[r]=1
            else:
                c=c+d[r]
                d[r]+=1
            if(r==0):
                c=c+1
        return c