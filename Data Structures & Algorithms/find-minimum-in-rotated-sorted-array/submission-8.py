class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        elif nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                if nums[mid+1] < nums[mid]:
                    return nums[mid+1]
                left = mid + 1
            elif nums[mid] < nums[right]:
                if mid == 0 or (mid > 0 and nums[mid-1] > nums[mid]):
                    return nums[mid]
                else:
                    right = mid - 1
            

            
                
                
