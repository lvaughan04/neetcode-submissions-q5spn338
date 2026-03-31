class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for num in hand:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        keyHeap = [i for i in count.keys()]
        heapq.heapify(keyHeap)

        while keyHeap:
            ## get the minimum value of the group
            start = keyHeap[0]
            length = 1
            count[start] -= 1
            if count[start] == 0:
                if keyHeap[0] == start:
                    heapq.heappop(keyHeap)
                    count.pop(start)
                else:
                    return False

            while length < groupSize:
                ## check if the next number exists in count
                if start + 1 in count:
                    start = start + 1
                    count[start] -= 1
                    if count[start] == 0:
                        ## check if you can pop it
                        if keyHeap[0] == start:
                            heapq.heappop(keyHeap)
                            count.pop(start)
                        else:
                            return False
                    length += 1
                else:
                    return False
        return True
