class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ro=len(matrix)
        c=len(matrix[0])
        r=[]
        for i in range(c):
            r.append([0]*ro)
        for i in range(ro):
            for j in range(c):
                r[j][i]=matrix[i][j]
        return r