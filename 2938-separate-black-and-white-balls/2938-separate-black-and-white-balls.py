class Solution:
    def minimumSteps(self, s: str) -> int:
        w=0
        sc=0
        for i in range(len(s)):
            if s[i]=='0':
                sc=sc+w
            else:
                w=w+1
        return sc