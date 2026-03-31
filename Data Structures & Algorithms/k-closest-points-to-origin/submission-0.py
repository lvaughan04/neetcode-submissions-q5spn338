class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ## we go through each pair in points and calculate the euclidean distance from (0,0) and then add that result to a min heap

        ## the while k, pop from min heap and add it to results array and then return results array

        ## quick problem. The min heap is storing the euclidian distance but we need to get the values of the coordinates so we could either use algebra to
        ## undo the work to get x1 and y1 or just store the euclidian value in a hashmap and then when we pop we check the hashmap of the indices that is store as a tuple
        minHeap = []
        values = defaultdict(list)
        res = []
        for x , y in points:
            ## calculate the distance
            distance = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(minHeap, distance)
            # if distance not in values:
            #     values[distance] = (x, y)
            values[distance].append((x , y))

        while k > 0:
            distance = heapq.heappop(minHeap)
            x , y = values[distance].pop()
            res.append([x, y])
            k -= 1
        return res
