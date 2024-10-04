class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i=0
        j=len(skill)-1
        t=skill[0]+skill[-1]
        c=0
        
        while(i<j):
            if skill[i]+skill[j]!=t:
                return -1
            else:
                c+=skill[i]*skill[j]
                i+=1
                j-=1
        return c
                