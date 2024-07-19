class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        l=[]
        c=[]
        r=[]
        for i in range(len(matrix)):
            l.append(min(matrix[i]))
        for j in range(len(matrix[0])):
            maxi=0
            for i in range(len(matrix)):
                if matrix[i][j]>maxi:
                    maxi=matrix[i][j]
            c.append(maxi)
        for i in l:
            if i in c:
                r.append(i)
        return r