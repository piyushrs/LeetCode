# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        c = [(j,i) for i,j in Counter(words).items()]
        c.sort(key = lambda x:(-x[0], x[1]))
        return [j for i, j in c[:k]]
    
words = ["i","love","leetcode","i","love","coding"]
k = 2

s = Solution()
print(s.topKFrequent(words, k))