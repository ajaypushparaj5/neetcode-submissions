class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        size=[]
        for i in strs:
            size.append(len(i))
        res=[]
        for i in size:
            res.append(str(i))
            res.append(",")
        res.append("#")
        res.extend(strs)
        return ''.join(res)


    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        size,res=[],[]
        i=0
        while(s[i]!='#'):
            j=i
            while(s[j]!=','):
                j+=1
            size.append(int(s[i:j]))
            i=j+1 
        i+=1
        for sz in size:
            res.append(s[i:i + sz])
            i += sz
        return res
            

