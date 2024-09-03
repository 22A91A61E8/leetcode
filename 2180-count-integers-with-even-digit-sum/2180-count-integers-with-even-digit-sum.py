class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(2,num+1):
            if sum([int(j) for j in str(i)])%2==0:
                c=c+1
        return c