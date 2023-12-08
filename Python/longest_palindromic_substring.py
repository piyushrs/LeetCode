class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = 0
        R = 0
        for i in range (1, n - 1):
            i_mirror = 2 * C - i
            if R > i:
                P[i] = min(R - i, P[i_mirror])
            else:
                P[i] = 0

            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        maxLen, centerIndex = max((P[i], i) for i in range(1, n - 1))
        return s[(centerIndex  - maxLen)//2 : (centerIndex + maxLen)//2]
    
a = Solution()
print(a.longestPalindrome("abacda"))