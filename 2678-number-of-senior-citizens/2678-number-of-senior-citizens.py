class Solution:
    def countSeniors(self, details: List[str]) -> int:
        l=[]
        c=0
        for i in range(len(details)):
            r=details[i]
            l.append(r[11:13])
        #print(l)
        for i in range(len(l)):
            if int(l[i])>60:
                c=c+1
        return c