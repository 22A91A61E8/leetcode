class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        l=[]
        l2=[]
        for i in range(len(matrix)):
            l.append(min(matrix[i]))
        #print(l)
        t_m=zip(*matrix)
        mc=[max(col) for col in t_m]
        l=[num for num in l if num in mc]
        return l