class Solution:
    def intersection(self, nums1, nums2):
        res = []
        i, j = 0, 0
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(set(res))
    
s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersection(nums1, nums2))