class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        low = 0
        high = len(numbers) -1

        for num in numbers:
            sum = numbers[low] + numbers[high]
            if(sum == target):
                return [low + 1, high + 1]

            if(sum > target): 
                high = high - 1
            elif (sum < target): 
                low = low + 1






        # start of with two pointers: low and high
        # essentially you have to loop through the array, and add 2 numbers together
        # during every loop. If the number is bigger than the target then the pointers 
        # must be updated accordingly
        # if num > target : high = high - 1
        # if num < target : low = low + 1

