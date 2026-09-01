class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left = 0
        right = len(heights)-1
        while (left< right):
            left_height = heights[left]
            right_height = heights[right]
            current_ans = min(left_height, right_height) * (right-left)
            if current_ans>ans:
                ans = current_ans
            if left_height>right_height:
                right-=1
            else:
                left+=1
        return ans
        