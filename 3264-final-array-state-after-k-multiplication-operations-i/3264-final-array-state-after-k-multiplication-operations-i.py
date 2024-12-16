class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while(k):
            r=min(nums)
            p=nums.index(r)
            nums[p]=r*multiplier
            k=k-1
        return nums