class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k=len(nums1)
        if n>0:
            nums1[-k:]=nums2
            nums1.sort()