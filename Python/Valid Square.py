# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        from math import dist
        a = dist(tuple(p1), tuple(p2))
        b = dist(tuple(p2), tuple(p3))
        c = dist(tuple(p3), tuple(p4))
        d = dist(tuple(p4), tuple(p1))
        e = dist(tuple(p1), tuple(p3))
        f = dist(tuple(p2), tuple(p4))

        if len({a,b,c,d,e,f}) == 2 and 0 not in {a,b,c,d,e,f}:
            return True
        else:
            return False
        
s = Solution()
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
print(s.validSquare(p1, p2, p3, p4))