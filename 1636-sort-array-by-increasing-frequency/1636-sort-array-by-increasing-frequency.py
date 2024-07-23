class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        m={}
        for num in nums:
            if num not in m:
                m[num]=1
            else:
                m[num]+=1
        
        freq=[]
        
        for x in m.values():
            freq.append(x)
        freq.sort()
        ans=[]
        for i in range(len(freq)):
            for key in m:
                if freq[i]==m[key]:
                    for i in range(freq[i]):
                        ans.append(key)
                    del m[key]
                    break
        return ans
