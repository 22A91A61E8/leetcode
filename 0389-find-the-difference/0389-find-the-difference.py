class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l=[]
        l1=[]
        for i in s:
            l.append(ord(i))
           
            #print(r)
        for i in t:
            l1.append(ord(i))
            
        k=abs(sum(l)-sum(l1))
            #print(k)
        return(chr(k))