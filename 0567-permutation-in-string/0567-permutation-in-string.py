class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        se1=[0]*26
        se2=[0]*26
        for i in range(len(s1)):
            se1[ord(s1[i]) - ord('a')] += 1
            se2[ord(s2[i])- ord('a')] += 1
        for i in range(len(s1), len(s2)):
            if se1 == se2:
                return True
            se2[ord(s2[i]) - ord('a')] += 1
            se2[ord(s2[i - len(s1)]) - ord('a')] -= 1
        return se1 == se2