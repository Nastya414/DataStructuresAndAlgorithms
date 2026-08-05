class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for number in nums:
            if number in dict1:
                dict1[number]+=1
            else:
                dict1[number]=1
        sorted_data = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
        return(list(sorted_data.keys())[:k])