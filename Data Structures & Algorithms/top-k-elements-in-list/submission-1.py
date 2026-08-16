from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        # l=list()
        # for i in range(k):
        #     top = 0
        #     for key,values in d.items():
        #         if values>top:
        #             top=values
        #             x=key
        #     l.append(x)
        #     del d[x]    
        # return l
        arr=[]
        for key,value in d.items():
            arr.append([value,key])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res               
                
                
            
        
