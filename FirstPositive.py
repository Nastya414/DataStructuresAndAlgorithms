class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
# for list [6,8,12,14] returns 1
    
        s_nums = []
        for n in nums:
            if n >= 1:
                s_nums.append(n)
        sorted_nums = sorted(set(s_nums))
        if len(sorted_nums) == 0:
            return 1
        elif sorted_nums[0]!=1:
            return 1
        elif sorted_nums[0]==1 and len(sorted_nums)==1:
            return 2
        for i in range(len(sorted_nums) - 1):
            num1 = sorted_nums[i]
            num2 = sorted_nums[i + 1]
            diff = num2 - num1
            if i == (len(sorted_nums) - 2) and diff == 1:
                return num2 + 1
            elif diff <= 1:
                continue
            elif diff > 1:
                return num1 + 1

# for list [6,8,12,14] returns 7

        s_nums = []
        for n in nums:
            if n >= 1:
                s_nums.append(n)
        sorted_nums = sorted(set(s_nums))
        if len(sorted_nums) == 0:
            return 1
        elif len(sorted_nums) == 1:
            return sorted_nums[0] + 1
        for i in range(len(sorted_nums) - 1):
            num1 = sorted_nums[i]
            num2 = sorted_nums[i + 1]
            diff = num2 - num1
            if i == (len(sorted_nums) - 2) and diff == 1:
                return num2 + 1
            elif diff <= 1:
                continue
            elif diff > 1:
                return num1 + 1

        