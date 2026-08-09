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