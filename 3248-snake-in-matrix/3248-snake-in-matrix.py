class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row,col=0,0
        for i in commands:
            if i=="UP":
                row=row-1
            elif i=="DOWN":
                row+=1
            elif i=="LEFT":
                col-=1
            elif i=="RIGHT":
                col+=1
        f=(row*n)+col
        return f
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 