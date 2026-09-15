class Solution(object):
    def maxProfit(self, prices):
                
        minprices = prices[0]
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprices:
                minprices = prices[i]
            elif prices[i] - minprices>maxprofit:
                maxprofit = prices[i] - minprices
        return maxprofit
 
        