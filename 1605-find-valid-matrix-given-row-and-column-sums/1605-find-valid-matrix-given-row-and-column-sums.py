class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        r =len(rowSum)
        c = len(colSum)
        i = 0
        j = 0
        m = [[0] * c for _ in range(r)]  

        while i < r and j < c:
            v = min(rowSum[i], colSum[j])
            m[i][j] = v  
            rowSum[i] -= v
            colSum[j] -= v
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1

        return m  
