class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        prefix = ""
        for i,char in enumerate(s):
            prefix += char

            print("PREFIX: ", prefix)
            
            for j in [i + 1, i + 2]:
                print("(trying %d)"%(j - i))
                suffix = list(prefix[::-1])
                print("suffix: ", suffix)
                k = j
                while suffix and k < len(s):
                    print("trying %s vs %s"%(s[k], suffix[0]))
                    if s[k] != suffix[0]:
                        break
                    print("Match %s"%(s[k]))
                    suffix.pop()
                    k += 1

                n_matches = len(prefix) - len(suffix)
                print("%d MATCHES"%(n_matches))
                if n_matches == 0:
                    continue
                palindrome = s[j - n_matches:k]
                print("CANDIDATE: ", palindrome)
                print("-")
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
            print("----------")

            #break
        return longest_palindrome

                


                

            

print(Solution().longestPalindrome("abb"))
#print(Solution().longestPalindrome("bab"))
