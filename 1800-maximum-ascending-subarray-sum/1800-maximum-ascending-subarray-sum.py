class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi=0
        sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sum+=nums[i]

            else:
                maxi=max(maxi,sum)
                sum=nums[i]

        return max(maxi,sum)