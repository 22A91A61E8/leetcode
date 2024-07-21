class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c=0
        v=['a','e','i','o','u']
        for i in s:
            if i in v:
                c=c+1
        if(c==0):
            return False
        else:
            return True