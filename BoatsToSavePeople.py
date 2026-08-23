class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counts=0
        people.sort()
        l,r=0, len(people)-1
        while l<=r:
            csum=people[l]+people[r]
            if csum<limit:
                counts+=1
                l,r=l+1, r-1
            elif csum>limit:
                r-=1
                counts+=1
            else:
                counts+=1
                l,r=l+1, r-1
            if l==r:
                counts+=1
                break
        return counts