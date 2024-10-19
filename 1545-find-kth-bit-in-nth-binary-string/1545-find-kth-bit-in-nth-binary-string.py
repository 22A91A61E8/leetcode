class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        for i in range(2, n + 1):
            p=s
            t=""
            for i in p:
                if i=="1":
                    t+="0"
                else:
                    t+="1"
            r=t[::-1]
            s=s+"1"+r
        return(s[k-1])
