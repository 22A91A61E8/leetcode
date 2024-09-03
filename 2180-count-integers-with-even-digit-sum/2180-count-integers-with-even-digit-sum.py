class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(2,num+1):
            d=sum(int(digit) for digit in str(i))
            if d%2==0:
                c=c+1
        return c