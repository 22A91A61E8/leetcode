class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m,c = -1, 0
        for i in range(len(arr)):
            m = max(arr[i], m)
            if m == i:
                c += 1
        return c
      
        
            
    