class Solution:
    # Starting at index `i` in `str`, counts the number
    # of matching characters in reversed(prefix)
    def countMatches(self, s: str, i: int, prefix: str) -> int:
        s_idx = i
        prefix_idx = len(prefix) - 1
        while s_idx < len(s) and prefix_idx >= 0:
            if s[s_idx] != prefix[prefix_idx]:
                break
            s_idx += 1
            prefix_idx -= 1
        
        n_matches = len(prefix) - (prefix_idx + 1)
        return n_matches


    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        prefix = ""
        for i,char in enumerate(s):
            # We record the current prefix. We'll want to
            # match the reverse of this prefix.
            prefix += char

            # We'll search for palindromes starting at `i+1` and `i+2`
            # For offset=1, we handle cases like "abba"
            # For offset=2, we handle cases like "aba"
            for offset in [1, 2]:
                n_matches = self.countMatches(s, i + offset, prefix)
                if n_matches == 0:
                    continue
                
                palindrome = s[i - n_matches + 1:i + n_matches + offset]
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
        
        if s and not longest_palindrome:
            longest_palindrome = s[0]

        return longest_palindrome

                


                

            
#print(Solution().longestPalindrome("bab"))
#print(Solution().longestPalindrome("abb"))
#print(Solution().longestPalindrome("abba"))
#print(Solution().longestPalindrome("abbababb"))
#print(Solution().longestPalindrome("bbababba"))
#print(Solution().longestPalindrome("abcdef"))
print(Solution().longestPalindrome(""))

