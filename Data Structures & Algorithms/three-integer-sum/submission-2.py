class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # sort the array
        nums.sort()

        for i in range(len(nums)):
            # check for duplicate starting value
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # break early if the first element is greater than 0 because 
            # thats already the smallest value
            if nums[i] > 0:
                break
            
            left = i+1
            right = len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return res




