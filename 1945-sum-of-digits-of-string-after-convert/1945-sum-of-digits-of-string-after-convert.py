class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l=''
        for i in s:
            l+=str(ord(i)-ord('a')+1)
        while k>0:
            t=0
            for i in l:
                t=t+int(i)
            l=str(t)
            k=k-1
        return int(l)