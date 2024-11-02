class Solution:
    def isCircularSentence(self, s: str) -> bool:
        x=s.split()
        if x[0][0]!=x[-1][-1]:
            return False
        for i in range(len(x)-1):
            if x[i][-1]!=x[i+1][0]:
                    return False
        return True