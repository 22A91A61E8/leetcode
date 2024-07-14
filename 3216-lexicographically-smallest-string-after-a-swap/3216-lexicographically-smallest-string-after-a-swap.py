class Solution:
    def getSmallestString(self, s: str) -> str:
        l=list(s)
        for i in range(len(l)-1):
            if (int(l[i])%2==0 and int(l[i+1])%2==0 and l[i+1]<l[i]):
                l[i],l[i+1]=l[i+1],l[i]
                return ''.join(l)
            elif (int(l[i])%2!=0 and int(l[i+1])%2!=0 and l[i+1]<l[i]):
                l[i],l[i+1]=l[i+1],l[i]
                return ''.join(l)
        return ''.join(l)