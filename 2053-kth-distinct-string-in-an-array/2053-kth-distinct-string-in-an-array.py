class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l=[]
        for i in arr:
            if arr.count(i)==1:
                l.append(i)
                if len(l)==k:
                    return l[len(l)-1]
        return ""
                            