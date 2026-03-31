# Seems like the subproblems are either use that coin to decrease the amount, or skip and go to the next coin in the array

# if i were to use a dfs on this problem what would it look like
#                              -- 23
#                             13    18    22
#                 3.          8           12
#              --   --  2   -- 3 7     2   7.    11
#                      1
#                      0   



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
        

        