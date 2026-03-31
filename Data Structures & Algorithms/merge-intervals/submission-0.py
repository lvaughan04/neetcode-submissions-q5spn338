class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            endValue = output[-1][1]
            if start <= endValue:
                # output[-1][1]
                if end > endValue:
                    output[-1][1] = end
            else:
                output.append([start, end])
        
        return output