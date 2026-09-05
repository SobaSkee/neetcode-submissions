class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0


        for num in nums:
            if num-1 not in nums_set:
                current_num = num
                current_streak = 1

                while current_num+1 in nums_set:
                    current_num += 1
                    current_streak += 1
                if current_streak > longest:
                    longest = current_streak
        return longest
            