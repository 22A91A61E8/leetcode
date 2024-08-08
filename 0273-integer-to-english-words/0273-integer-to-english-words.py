class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        bs = ["Thousand", "Million", "Billion"]
        r = self.convertString(num % 1000)
        num //= 1000
        
        for i in range(len(bs)):
            if num % 1000 > 0:
                r = self.convertString(num % 1000) + " " + bs[i] + " " + r
            num //= 1000
        
        return r.strip()
    
    def convertString(self, n: int) -> str:
        d = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tn = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tns = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        r = ""
        
        if n > 99:
            r += d[n // 100] + " Hundred "
        n %= 100
        
        if 10 <= n < 20:
            r += tn[n - 10] + " "
        else:
            if n >= 20:
                r += tns[n // 10] + " "
            n %= 10
            if n > 0:
                r += d[n] + " "
        
        return r.strip()