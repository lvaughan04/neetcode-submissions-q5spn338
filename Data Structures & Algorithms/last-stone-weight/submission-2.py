class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heaviestStones = [-n for n in stones]
        heapq.heapify(heaviestStones)
    
        while heaviestStones:
            if len(heaviestStones) == 1:
                return -heaviestStones[0]

            first , second = -heapq.heappop(heaviestStones), -heapq.heappop(heaviestStones)
            if first == second:
                continue
            else:
                if first < second:
                    second -= first
                    heapq.heappush(heaviestStones, -second)
                else:
                    first -= second
                    heapq.heappush(heaviestStones, -first)
        return 0