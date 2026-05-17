class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxarea=0
        while left<right:
            length=min(heights[left],heights[right])
            area=length*(right-left)
            if maxarea<area:
                maxarea=area
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        return maxarea
        