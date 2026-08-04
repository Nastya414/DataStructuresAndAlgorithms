class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words_dict_list=[]
        for word in strs:
            letterdict={}
            for letter in word:
                if letter in letterdict:
                    letterdict[letter]+=1
                else:
                    letterdict[letter]=1
            words_dict_list.append([word,letterdict])
        grouped={}
        for w,d in words_dict_list:
            key=tuple(sorted(d.items()))
            if key in grouped:
                grouped[key].append(w)
            else:
                grouped[key]=[w]
        result=list(grouped.values())
        return result
