class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        for i in range(n):
            s=0
            for j in range(i,n):
                s=s+nums[j]
                l.append(s)
        l.sort()
        
        mod=10**9+7
        r=0
        for i in range(left-1,right):
            r+=l[i]
        #print(r)
        return r%mod
    