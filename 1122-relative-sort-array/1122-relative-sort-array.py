class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if(arr1[j]==arr2[i]):
                    l.append(arr1[j])
                    arr1[j]=-5
        arr1.sort()
        for n in arr1:
            if n!=-5:
                l.append(n)
        return l
            
                    
        