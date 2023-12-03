# You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fac = [1]
        if k == 1:
            return 1
        for i in range(2,n+1):
            # print(f"i in for loop: {i}")
            if n%i==0:
                fac.append(i)
                # print(f"appended {i} in fac list {fac}")
            if len(fac) == k:
                try:
                    return fac[k-1]
                except IndexError:
                    return -1
        return -1
    
s = Solution()
print(s.kthFactor(12, 3))
print(s.kthFactor(7, 2))
print(s.kthFactor(4, 4))