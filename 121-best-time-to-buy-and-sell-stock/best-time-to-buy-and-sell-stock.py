class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        pr=0;sell=prices[0]
        for i in range(1,len(prices)):
            sell=min(sell,prices[i])
            pr = max(pr,prices[i]-sell)
        return pr
        