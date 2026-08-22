class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i, a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            else:
                diff=0-a  
                l,r=i+1,len(nums)-1
                while l<r:
                    csum=nums[l]+nums[r]
                    if csum<diff:
                        l+=1
                    elif csum>diff:
                        r-=1
                    else:
                        result.append([a,nums[l], nums[r]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1
        return result