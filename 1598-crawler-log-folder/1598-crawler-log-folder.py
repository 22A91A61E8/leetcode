class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in logs:
            if i=="../":
                if c>0:
                    c=c-1
            elif i!="./":
                c=c+1
        return c