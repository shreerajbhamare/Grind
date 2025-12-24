class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t=sum(apple)
        capacity.sort(reverse=True)
        c=0
        for i in range(len(capacity)):
            c+=1
            t-=capacity[i]
            if t<=0:
                break
                
        return c        