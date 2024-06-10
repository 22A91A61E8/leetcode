class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        e=sorted(heights)
        c=0
        for i in range(len(heights)):
            if(heights[i]!=e[i]):
                c=c+1
        return c