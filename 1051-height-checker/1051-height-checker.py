class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #to create a newlist form existing should use always sorted() where as sort() will modify the existing one and return none
        e=sorted(heights)
        c=0
        for i in range(len(heights)):
            if(heights[i]!=e[i]):
                c=c+1
        return c