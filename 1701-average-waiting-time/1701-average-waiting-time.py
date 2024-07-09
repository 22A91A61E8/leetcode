class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        l=[]
        d=0
        for i in customers:
            p=i
            if d==0 or p[0]>d:
                d=p[0]+p[1]
            else:
                d=d+p[1]
            l.append(d-p[0])
        n=len(l)
        return (sum(l)/n)
        