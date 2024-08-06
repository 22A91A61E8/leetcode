class Solution:
    def minimumPushes(self, word: str) -> int:
        r=Counter(word)
        m=sorted(r.values(),reverse=True)
        s=0
        for i,j in enumerate(m):
            s+=((i//8)+1)*j
        return s
    