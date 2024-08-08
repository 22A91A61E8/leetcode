class Solution:
    def spiralMatrixIII(self, R: int, C: int, r: int, c: int) -> List[List[int]]:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        n, res, d, steps = R*C, [], 0, 1
      
        while len(res) < n:
            for _ in range(2):
                for _ in range(steps):
                    if 0 <= r < R and 0 <= c < C:
                        res.append([r, c])
                        if len(res) == n:
                            return res
                    r += dirs[d][0]
                    c += dirs[d][1]
                d = (d + 1) % 4
            steps += 1

        return res
