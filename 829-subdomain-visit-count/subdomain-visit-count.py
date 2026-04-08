class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ch_s= dict()
        for i in range(len(cpdomains)):
            num, domain = cpdomains[i].split()
            num = int(num)
            dm_arr = domain.split(".")
            dm_arr = dm_arr[::-1]
            for j in range(len(dm_arr)):
                if j==0:
                    if dm_arr[0] in ch_s:
                        ch_s[dm_arr[0]]+=num
                    else:
                        ch_s[dm_arr[0]]=num
                else:
                    dm_arr[j]=dm_arr[j]+"."+dm_arr[j-1]
                    dm = dm_arr[j]
                    if dm in ch_s:
                        ch_s[dm]+=num
                    else:
                        ch_s[dm]=num
        res=[]
        for i in ch_s:
            res.append(str(ch_s[i])+" "+i)
        return res
