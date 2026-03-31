class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for i in range(n - 2, -1, -1):
            tmp = one
            one = one + two
            two = tmp
        ## input =  5
        dp = [5, 3, 2, 1, 1]

        return one