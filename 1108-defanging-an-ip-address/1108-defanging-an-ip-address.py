class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
            if i!=".":
                ans=ans+i
            else:
                ans=ans+"[.]"
        return ans
        