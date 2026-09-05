class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        for i in range(len(heights)):
            left = heights[i]
            for j in range(i+1, len(heights)):
                height = min(left, heights[j])
                area = height * (j-i)
                if area > maxWater:
                    maxWater = area
        return maxWater

