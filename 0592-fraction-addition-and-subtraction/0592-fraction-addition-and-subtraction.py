from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        a=eval(expression)
        b=Fraction(a).limit_denominator(2**32) 
        if len(str(b))<=2:
            return str(b)+str("/1")
        return str(b)