class Solution:
    def scoreOfString(self, s: str) -> int:
        l=[]
        for i in range(1,len(s)):
            r=abs(ord(s[i])-ord(s[i-1]))
            l.append(r)
        return sum(l)