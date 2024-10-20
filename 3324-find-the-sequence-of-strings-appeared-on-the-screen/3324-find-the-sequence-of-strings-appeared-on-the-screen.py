class Solution:
    def stringSequence(self, target: str) -> List[str]:
        t=["a"]
        i=0
        j=0
        while(t[-1]!=target):
            if t[-1][i]==target[i]:
                t.append(t[-1][:j+1]+"a")
                i+=1
                j+=1
            else:
                t.append(t[-1][:j]+chr((ord(t[-1][j])+1)))
        return t
            
        