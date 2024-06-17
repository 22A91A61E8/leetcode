class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0;
        j=int (math.sqrt(c))
        while(i<=j):
            if (i*i+j*j==c):
                return True
            if (i*i+j*j>c):
                j=j-1
            else:
                i=i+1
        return False