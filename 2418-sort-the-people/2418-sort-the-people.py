class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        r=zip(names,heights)
        k=sorted(r,key=lambda x:x[1],reverse=True)
        return [names for names,heights in k] 