class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        t=sum(chalk)
        k=k%t
        for i in range(len(chalk)):
            if k<chalk[i]:
                return i
                break 
            k=k-chalk[i]