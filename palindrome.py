class Solution:
    def countMatches(self, s: str, prefix: str, i: int) -> int:
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
            prefix += char

            print("PREFIX: ", prefix)
            # check matches starting at i+1
            n_matches = self.countMatches(s, prefix, i + 1)
            if n_matches != 0:
                print("Matches 1st: %d"%(n_matches))
                palindrome = s[i - n_matches + 1:i + n_matches + 1]
                print("FOUND: ", palindrome)
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome

            # check matches starting at i+2
            n_matches = self.countMatches(s, prefix, i + 2)
            if n_matches != 0:
                print("Matches 2nd: %d"%(n_matches))
                palindrome = s[i - n_matches + 1:i + n_matches + 2]
                print("FOUND: ", palindrome)
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome

            print("-------")
            #break
        return longest_palindrome

                


                

            
print(Solution().longestPalindrome("bab"))
#print(Solution().longestPalindrome("abb"))
#print(Solution().longestPalindrome("abba"))
#print(Solution().longestPalindrome("abbababb"))
#print(Solution().longestPalindrome("bab"))
