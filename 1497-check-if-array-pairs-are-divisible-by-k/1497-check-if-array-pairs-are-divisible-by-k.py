class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d={}
        for i in arr:
            r=(i%k+k)%k
            d[r]=d.get(r,0)+1
           
        for i in d:
            if i==0:
                if d[i]%2!=0:
                    return False
            else:
                c=k-i
                if d.get(i,0)!=d.get(c,0):
                    return False
        return True