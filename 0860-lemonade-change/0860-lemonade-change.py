class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten=0
        five = 0
        for cash in bills:
            if cash == 5:
                five += 1
            elif cash == 10:
                ten += 1
                if five > 0:
                    five -= 1
                else:
                    return False
            elif cash == 20:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
        