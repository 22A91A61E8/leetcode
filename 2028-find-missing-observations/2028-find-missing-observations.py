class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        v=((len(rolls)+n)*mean)-sum(rolls)

        if v<n or v>n*6:
            return([])
        r=[1]*n
        v=v-n
        i=0
        while v>0:
            a=min(5,v)
            r[i]+=a
            v=v-a
            i+=1
        return r
