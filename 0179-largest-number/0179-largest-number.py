class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n=[str(num) for num in nums]
        n.sort(key=lambda a:a*10,reverse=True)
        if n[0]=="0":
            return "0"
        return "".join(n)