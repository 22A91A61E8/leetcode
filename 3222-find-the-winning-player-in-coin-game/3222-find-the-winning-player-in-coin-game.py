class Solution:
    def losingPlayer(self, x: int, y: int) -> str:

        c=0
        while x>=1 and y>=4:
            x=x-1
            y=y-4
            c=c+1
        if c%2==0:
            return "Bob"
        else:
            return "Alice"