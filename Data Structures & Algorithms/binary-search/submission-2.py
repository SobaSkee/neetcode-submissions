class Solution:
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # target 2
    # mid = 4


    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1