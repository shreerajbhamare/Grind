class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]*len(nums);r=[1]*len(nums)
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            r[i]=r[i+1]*nums[i+1]
        print(l,r)
        for i in range(len(nums)):
            l[i]*=r[i]
        return l
        
        