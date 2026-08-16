class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r=0,0
        output=[]
        while l<len(word1) and r<len(word2):
            output.append(word1[l]+word2[r])
            l, r=l+1, r+1
        output.append(word1[l:])
        output.append(word2[r:])
        final_string="".join(output)
        return final_string