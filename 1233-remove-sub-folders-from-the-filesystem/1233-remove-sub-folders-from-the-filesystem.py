class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        r=[folder[0]]
        for i in range(1,len(folder)):
            l=r[-1]
            l+="/"
            if not folder[i].startswith(l):
                r.append(folder[i])
        return r