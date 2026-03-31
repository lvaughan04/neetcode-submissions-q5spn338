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
            print("left is ", nums[left])
            print("right is ", nums[right])
            print("mid is ", nums[mid])
            if nums[mid] > nums[right]:
                if mid != len(nums) and nums[mid+1] < nums[mid]:
                    return nums[mid+1]
                left = mid + 1
            elif nums[mid] < nums[right]:
                if mid == 0 or (mid > 0 and nums[mid-1] > nums[mid]):
                    return nums[mid]
                else:
                    right = mid - 1
            else:
                return nums[mid]
            print("After")
            print("left is ", nums[left])
            print("right is ", nums[right])
            print("mid is ", nums[mid])
            
                
                
