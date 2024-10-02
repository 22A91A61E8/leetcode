class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        p=sorted(arr)
        d={}
        c=1
        for i in p:
            if i not in d:
                d[i]=c
                c+=1
        l=[]
        for i in arr:
            l.append(d[i])
        return l