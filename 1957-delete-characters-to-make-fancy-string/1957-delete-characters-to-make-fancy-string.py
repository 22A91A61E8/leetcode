class Solution:
    def makeFancyString(self, s: str) -> str:
        n=len(s)
        s=list(s)
        for i in range(n-2):
            if s[i]==s[i+1]==s[i+2]:
                s[i]="_"
        return "".join(i for i in s if i!="_")
       