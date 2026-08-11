class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1=sorted(set(nums))
        counts=1
        result_list=[]
        if len(nums1)==1:
            result_list.append(1)
        elif len(nums1)==0:
            result_list.append(0)
        for i in range(len(nums1)-1):
            num1=nums1[i]
            num2=nums1[i+1]
            diff=num2-num1
            if i==len(nums1)-2 and diff==1:
                counts+=1
                result_list.append(counts)
                break
            elif i==len(nums1)-2 and diff!=1:
                result_list.append(counts)
                break
            elif diff==1:
                counts+=1
            elif diff!=1:
                result_list.append(counts)
                counts=1
                continue
        result=max(result_list)
        return result