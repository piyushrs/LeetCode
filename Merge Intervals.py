# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals):
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        
        for i in intervals[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
        
        return stack
    
intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output = [[1, 6], [8, 10], [15, 18]]
s = Solution()
print(s.merge(intervals))