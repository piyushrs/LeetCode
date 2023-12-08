from collections import defaultdict
import math
class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n == 1:
            return 1
        
        result = 2
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1

            result = max(result, max(cnt.values())+1)
        
        return result
    
s = Solution()
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
print(s.maxPoints(points))