class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        c=0; prev = 10e9; ans=0
        for i in range(0, len(prices)):
            if prices[i]==prev-1:
                c+=1
            else:
                ans+=(c*(c+1))//2
                c=1
            prev=prices[i]
        ans+=(c*(c+1))//2
        return ans

        