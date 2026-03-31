class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-n for n in counter.values()]
        heapq.heapify(heap)
        queue = deque() # [value, time to move back to heap]
        time = 0
        while heap or queue:
            time += 1
            if heap:
                value = 1 + heapq.heappop(heap)
                if value < 0:
                    queue.append([value, time + n])
            if queue:
                if queue[0][1] == time:
                    heapq.heappush(heap, queue.popleft()[0])
        return time
                



        
