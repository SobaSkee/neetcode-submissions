class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            else:
                # binary search
                m = (l+r) // 2
                # part of left sorted portion
                if nums[m] >= nums[l]:
                    l = m+1
                # part of the right portion
                else:
                    r = m-1
                res = min(res, nums[m])

        return res

    # every value in the right sorted portion is smaller
    # than every value in the left sorted portion because this is a rotated
    # sorted array otherwise it would just be a regular sorted array