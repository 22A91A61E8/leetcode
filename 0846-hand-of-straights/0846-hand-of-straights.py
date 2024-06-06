class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize!=0):
            return False
        c=Counter(hand)
        s=sorted(c.keys())
        for key in s:
            if c[key]>0:
                s_c=c[key]
                for i in range(key, key + groupSize):
                    if c[i] < s_c:
                        return False
                    c[i] -= s_c
        
        
        return True
