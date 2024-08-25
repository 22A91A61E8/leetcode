class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            r=min(nums)
            i=nums.index(r)
            nums[i]=r*multiplier
        return nums