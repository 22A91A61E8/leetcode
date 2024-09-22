class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        c=0
        s=set(bannedWords)
        for i in message:
            if i in s:
                c=c+1
                if(c>=2):
                    return True
            