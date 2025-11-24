class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=0;maxs=-inf
        for i in range(len(nums)):
            summ+=nums[i]
            maxs=max(summ,maxs)
            summ=(max(0,summ))
        return maxs