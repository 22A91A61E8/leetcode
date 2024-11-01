class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        s=list(s)
        for i in range(n-2):
            if s[i]==s[i+1]==s[i+2]:
                s[i]="_"
                
        l=[]
        for i in s:
            if i!="_":
                l.append(i)
        return "".join(l)