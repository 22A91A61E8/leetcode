class Solution:
    def capitalizeTitle(self, title: str) -> str:
        r=title.split()
        j=[]
        for i in r:
            if len(i)>2:
                k=i.title()
                j.append(k)
            else:
                k=i.lower()
                j.append(k)
        return ' '.join(j)
        