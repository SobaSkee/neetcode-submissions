class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        left = 0
        right = len(heights)-1



        for i in range(len(heights)):

            area = min(heights[left], heights[right]) * (right - left)

            if area > maxWater:
                maxWater = area
            if heights[left] < heights[right] or heights[left] == heights[right]:
                left += 1
            else:
                right -= 1
                
            
        return maxWater

