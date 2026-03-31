class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        [1,2,1,2,1,1,1]
        [4,5,3,3,2,1,1]
        one = cost[1]
        two = cost[0]
        for i in range(2, len(cost)):
            ## since it starts at the [-2] pos in the array
            tmp = one
            one = cost[i] + min(one, two)
            two = tmp
        return min(one, two)