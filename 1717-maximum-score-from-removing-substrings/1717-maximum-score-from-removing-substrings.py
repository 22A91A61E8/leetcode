class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def find_pairs(s,p,k):
            score=0
            stack=[]

            for i in s:
                if stack and stack[-1]==p[0] and i==p[1]:
                    stack.pop()
                    score=score+k
                else:
                    stack.append(i)
            return ''.join(stack),score
            
        if x>y:
            p,i,p1,j="ab",x,"ba",y
        else:
            p,i,p1,j="ba",y,"ab",x
    
        s,h_s=find_pairs(s,p,i)
        s,l_s=find_pairs(s,p1,j)
        return (h_s+l_s)