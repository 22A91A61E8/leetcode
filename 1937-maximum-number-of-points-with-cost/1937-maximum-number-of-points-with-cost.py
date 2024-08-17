class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        ps = points[0]
        
        for i in range(1, n):
            cs = [0] * m
            
            lm = [float('-inf')] * m
            rm = [float('-inf')] * m
            
            lm[0] = ps[0]
            for j in range(1, m):
                lm[j] = max(lm[j - 1], ps[j] + j)
            
            rm[m - 1] = ps[m - 1] - (m - 1)
            for j in range(m - 2, -1, -1):
                rm[j] = max(rm[j + 1], ps[j] - j)
            
            for j in range(m):
                cs[j] = points[i][j] + max(lm[j] - j, rm[j] + j)
            ps = cs
        return max(ps) 