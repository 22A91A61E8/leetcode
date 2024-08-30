class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d=set()
        c=0
        for i in word:
            if i.lower() in d:
                continue
            if i.lower() in word and i.upper() in word:
                c=c+1
                d.add(i.lower())
        return c