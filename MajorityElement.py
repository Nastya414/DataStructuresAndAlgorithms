class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        halflen=(len(nums))/2
        for n in nums:
            if n in dict1:
                dict1[n]+=1
            else:
                dict1[n]=1
        for k, v in dict1.items():
            if v>halflen:
                return (k)

#for numbers that appear more than n/3 times
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        dict1={}
        for n in nums:
            if n in dict1:
                dict1[n]+=1
            else:
                dict1[n]=1
        target_n=len(nums)/3
        for k, v in dict1.items():
            if v>target_n:
                result.append(k)  
        return result