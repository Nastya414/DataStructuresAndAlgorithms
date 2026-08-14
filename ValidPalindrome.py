class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        left=0
        right=len(s1)-1
        is_palindrome=True
        while left<right:
            if s1[right]!=s1[left]:
                is_palindrome=False
            left+=1
            right-=1
        return(is_palindrome)