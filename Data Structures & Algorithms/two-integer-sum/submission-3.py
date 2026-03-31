class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Result map will store the index as its key and the value as it actual number
        ## So like {0: 3, 1:4, 2:5, 3:6}
        ## Check if difference of the current number is in the map and if not add it to the map
        ## If it is, return the indicies

        result = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in result:
                return [result[diff], i] 
            else:
                result[nums[i]] = i
        return []