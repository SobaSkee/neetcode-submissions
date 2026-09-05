class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # -4, -1, -1, 0, 1, 2

        res = []

        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            else:
                seen.add(nums[i])
                l = i+1
                r = len(nums)-1
                while l < r:
                    total = nums[i] + nums[l] + nums[r]
                    if total < 0:
                        l += 1
                    elif total > 0:
                        r -= 1
                    else:
                        candidate = [nums[i], nums[l], nums[r]]
                        if candidate not in res:
                            res.append(candidate)
                        l += 1
                        r -= 1
        return res
                

