class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n1 = nums.count(1)
        n = len(nums)
        sum_range = sum(nums[:n1])
        max_sum_range = sum_range
        for remove, add in zip(nums, nums[n1:] + nums[:n1]):
            delta = add - remove
            sum_range += delta
            if sum_range > max_sum_range:
                max_sum_range = sum_range
        return n1 - max_sum_range
        