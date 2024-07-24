class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        dict1 = {}
        lst = []
        strn = ""
        val = []
        for i in range(len(mapping)):
            dict1[i] = mapping[i]
        for num in nums:
            num = str(num)
            strn=""
            for n in num:
                strn += str(dict1[int(n)])
            #dict2[int(num)] = int(strn)
            lst.append([int(num),int(strn)])
        lst.sort(key = lambda x:x[1])
        #dict2 = dict(sorted(dict2.items(), key = lambda x:x[1]))
        return [lst[i][0] for i in range(len(lst)) ]
