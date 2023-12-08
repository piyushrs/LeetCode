# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height):
        n = len(height)
        left = [0]*n
        right = [0]*n
        water = 0
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        right[n-1] = height[n-1]
        # print(f"Right before update: {right}")
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
            # print(f"Right while in for loop: {right}")
        
        for i in range(0, n):
            water += min(left[i], right[i]) - height[i]
            # print(f"Water updates: {water}")
        
        # print(left)
        # print(f"Right after update: {right}")
        return water
    
s = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))