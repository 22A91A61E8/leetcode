class Solution:
    def minSteps(self, n: int) -> int:
        s=0
        f=2
        while n>1:
            while n%f==0:
                s+=f
                n=n//f
            f=f+1
        return s