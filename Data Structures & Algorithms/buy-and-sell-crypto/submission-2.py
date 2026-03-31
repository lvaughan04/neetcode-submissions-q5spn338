class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for price in prices:
            ## see if price is less than the lowest
            ## if it is, then lowest becomes the new and continue
            ## check if price - lowest is bigger than current profit
            if price < lowest:
                lowest = price
                continue
            cur = price - lowest
            profit = max(cur, profit)


        return profit