class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1 for i in range(len(prices))] for i in range(2)]for i in range(2)]
        return self.backpack(prices,dp,0,0,0)

    
    def backpack(self, prices,dp,idx,can_sell,num_transaction):
        if num_transaction>=2: return 0
        if idx>=len(prices): return 0
        if dp[num_transaction][can_sell][idx]!=-1: return dp[num_transaction][can_sell][idx]
        if can_sell==1:
            pr_by_sell = self.backpack(prices,dp,idx+1,0,num_transaction+1) + prices[idx]
            pr_by_hold = self.backpack(prices,dp,idx+1,1,num_transaction)
            dp[num_transaction][can_sell][idx]=max(pr_by_sell,pr_by_hold)
        else:
            pr_by_buy = self.backpack(prices,dp,idx+1,1,num_transaction) - prices[idx]
            pr_by_ignore = self.backpack(prices,dp,idx+1,0,num_transaction)
            dp[num_transaction][can_sell][idx]=max(pr_by_buy,pr_by_ignore)
        return dp[num_transaction][can_sell][idx]