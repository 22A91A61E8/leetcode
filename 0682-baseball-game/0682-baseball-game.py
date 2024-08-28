class Solution:
    def calPoints(self, operations: List[str]) -> int:
        r = []
        for op in operations:
            if op == "C":
                if r:
                    r.pop()
            elif op == "+":
                if len(r) >= 2:
                    r.append(r[-1] + r[-2])
            elif op == "D":
                if r:
                    r.append(r[-1] * 2)
            else:
                 
                r.append(int(op))
        
        return sum(r)