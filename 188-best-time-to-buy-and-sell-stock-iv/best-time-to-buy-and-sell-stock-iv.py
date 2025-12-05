class Solution:
    def maxProfit(self, k, prices) -> int:
        dp = [[[-1 for i in range(len(prices))] for i in range(2)]for i in range(k)]
        return self.backpack(prices,dp,0,0,0,k)

    
    def backpack(self, prices,dp,idx,can_sell,num_transaction,k):
        if num_transaction>=k: return 0
        if idx>=len(prices): return 0
        if dp[num_transaction][can_sell][idx]!=-1: return dp[num_transaction][can_sell][idx]
        if can_sell==1:
            pr_by_sell = self.backpack(prices,dp,idx+1,0,num_transaction+1,k) + prices[idx]
            pr_by_hold = self.backpack(prices,dp,idx+1,1,num_transaction,k)
            dp[num_transaction][can_sell][idx]=max(pr_by_sell,pr_by_hold)
        else:
            pr_by_buy = self.backpack(prices,dp,idx+1,1,num_transaction,k) - prices[idx]
            pr_by_ignore = self.backpack(prices,dp,idx+1,0,num_transaction,k)
            dp[num_transaction][can_sell][idx]=max(pr_by_buy,pr_by_ignore)
        return dp[num_transaction][can_sell][idx]