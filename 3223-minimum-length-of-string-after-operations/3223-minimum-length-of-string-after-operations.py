class Solution:
    def minimumLength(self, s: str) -> int:
        d={}
        c=0
        for i in s:
            if i not in d:
                d[i]=0
            d[i]+=1
            if d[i]==3:
                d[i]=d[i]-2
                c=c+2
        return len(s)-c
                
 