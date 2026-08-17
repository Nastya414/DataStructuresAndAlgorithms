#returns a new list
nums=list(map(int, input().split()))
l,r=1,2
result=[nums[0]]
while r<len(nums):
    if nums[l]!=nums[r]:
        result.append(nums[r])
    l, r=l+1, r+1
print(result)

#return number of unique values and nums variable has only unique values
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1, len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l+=1
        return l

