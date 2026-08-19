class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        result=[1]*len(nums)
        for i in range(len(nums)):
            result[i+k%len(nums)-len(nums)]=nums[i]
        nums[:]=result