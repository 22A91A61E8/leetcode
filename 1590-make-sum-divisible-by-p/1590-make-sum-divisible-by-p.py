class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ts=sum(nums)
        rem=ts%p
        if rem==0:
            return 0
        pm={0:-1}
        ps=0
        l=len(nums)
        for i , num in enumerate(nums):
            ps+=num
            cm=ps%p
            tm=(cm-rem+p)%p
            if tm in pm:
                l=min(l,i-pm[tm])
            pm[cm]=i
        if l < len(nums):
            return l
        else:
            return -1