class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag=0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                break
            else:
                if i==0:
                    flag=1
                digits[i]=0
        if flag:
            digits.insert(0,1)
        return(digits)
        