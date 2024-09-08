class Solution:
    def convertDateToBinary(self, date: str) -> str:
        d=date.split('-')
        k=[]
        for i in d:
            k.append(bin(int(i))[2:])
        return '-'.join(k)