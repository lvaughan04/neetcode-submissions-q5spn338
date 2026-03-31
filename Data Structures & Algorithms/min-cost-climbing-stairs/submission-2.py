class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## recurrence relation = cost[i] + min(cost[i-2], cost[i - 1])
        one = two = 1
        [1, 2, 4, 5]
        [1, 2, 1, 2, 1,1,1]
         #4  5  3  3, 2
        print(cost)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        print(cost)
        return min(cost[0], cost[1])