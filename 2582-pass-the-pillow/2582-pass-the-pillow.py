class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        e=time%(2*(n-1))
        if e<n:
            return e+1
        else:
            return 2*n-1-e