class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        res=""
        num1 = "{:04d}".format(num1)
        num2 = "{:04d}".format(num2)
        num3 = "{:04d}".format(num3)
        for i in range(4):
            res += min(num1[i],num2[i],num3[i])
        return (int(res))