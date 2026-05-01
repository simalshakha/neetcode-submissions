class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        left=pre=l=prices[0]
        
        for i,price in enumerate(prices[0:]):
            # if pre<prices[i]:
            #     l=prices[i]
            #     left+=i
            if price-left>profit:
                profit =price-left
            if price<left:
                left =price

        return profit
       
            
   

                
            
        