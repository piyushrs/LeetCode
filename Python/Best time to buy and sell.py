class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
          if prices[i] < min_price:
            min_price = prices[i]
          else:
            max_profit = max(prices[i]-min_price, max_profit)
        return max_profit
    
s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))