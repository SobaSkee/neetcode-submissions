class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []
        for index, num in enumerate(nums):
            otherVal = target - num
            if otherVal not in hashmap:
                hashmap[num] = index
            else:
                res.append(hashmap[otherVal])
                res.append(index)
        return res