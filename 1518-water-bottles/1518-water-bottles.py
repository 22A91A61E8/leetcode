class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        t_d=numBottles
        e_b=numBottles
        while e_b>=numExchange:
            n_b=e_b//numExchange
            t_d=t_d+n_b
            e_b=e_b%numExchange+n_b
        return t_d