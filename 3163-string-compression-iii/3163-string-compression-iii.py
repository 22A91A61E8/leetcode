class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        n = len(word)
        i = 0
        c = 1
        
        while i < n - 1:
            if word[i] == word[i + 1] and c < 9:
                c += 1
            else:
                comp.append(str(c) + word[i])
                c = 1
            i += 1

        comp.append(str(c) + word[i])  
        return ''.join(comp)