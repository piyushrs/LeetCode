class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i in range(len(mat)):
            if i not in d.keys():
                d[i] = sum(mat[i])
                
        return list({i: j for i, j in sorted(d.items(), key=lambda item: item[1])}.keys())[:k]