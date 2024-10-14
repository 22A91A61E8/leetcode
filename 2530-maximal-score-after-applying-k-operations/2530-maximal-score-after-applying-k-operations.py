class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        mh=[-i for i in nums]
        heapq.heapify(mh)
        v=0
        for _ in range(k):
            mv=-heapq.heappop(mh)
            v=v+mv
            p=math.ceil(mv/3)
            heapq.heappush(mh,-p)
        return v
            
            
            