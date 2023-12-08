class Solution:
    def numberOfBoomerangs(self, points):
        count = 0
        for i in points:
            d = {}
            for j in points:
                dist = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                d[dist] = d.get(dist, 0) + 1
                # print(d)
            for k in d:
                count += d[k] * (d[k] - 1)
        return count
    
s = Solution()
points = [[0,0],[1,0],[2,0]]
print(s.numberOfBoomerangs(points))