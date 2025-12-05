class Solution:
    def maxProfit(self, prices: List[int],fee) -> int:
        dp = [[-1 for i in range(len(prices))] for i in range(2)]
        return self.backpack(prices,dp,0,0,fee)

    
    def backpack(self, prices,dp,idx,can_sell,fee):
        if idx>=len(prices): return 0
        if dp[can_sell][idx]!=-1: return dp[can_sell][idx]
        if can_sell==1:
            pr_by_sell = self.backpack(prices,dp,idx+1,0,fee) + prices[idx] - fee
            pr_by_hold = self.backpack(prices,dp,idx+1,1,fee)
            dp[can_sell][idx]=max(pr_by_sell,pr_by_hold)
        else:
            pr_by_buy = self.backpack(prices,dp,idx+1,1,fee) - prices[idx]
            pr_by_ignore = self.backpack(prices,dp,idx+1,0,fee)
            dp[can_sell][idx]=max(pr_by_buy,pr_by_ignore)
        return dp[can_sell][idx]