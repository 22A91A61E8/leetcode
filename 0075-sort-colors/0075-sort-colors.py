class Solution:
    def sortColors(self,arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        for i in range(len(arr)):
            for j in range(0,len(arr)-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr      