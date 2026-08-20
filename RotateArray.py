class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        result=[1]*len(nums)
        for i in range(len(nums)):
            result[i+k%len(nums)-len(nums)]=nums[i]
        nums[:]=result

#second solution
k=k%len(nums)
nums.reverse()
nums[:k]=reversed(nums[:k])
nums[k:]=reversed(nums[k:])

#or by using two pointers
k=k%len(nums)
l,r=0, len(nums)-1
while l<r:
    nums[l], nums[r]= nums[r], nums[l]
    l,r=l+1, r-1
l,r=0, k-1
while l<r:
    nums[l], nums[r]= nums[r], nums[l]
    l,r=l+1, r-1
l,r=k, len(nums)-1
while l<r:
    nums[l], nums[r]= nums[r], nums[l]
    l,r=l+1, r-1