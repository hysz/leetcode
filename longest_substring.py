from pprint import pprint

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)

        '''
        We construct a lookup table that allows you to query for next occurence of a character.
        We use len(s) to denote a non-existent index.
        Ex for string "abab"
            {
                "a:
                {
                    0: 2,
                    2: len(s),
                    -1: 2   // Used to lookup furthest occurence
                },
                "b":
                {
                    1: 3,
                    3: len(s)
                }
            }
        '''

        # construct lookup
        lookup = {}
        for i,c in enumerate(s):
            if not c in lookup:
                lookup[c] = {}
                l = lookup[c]
                l[i] = len(s)
                l[-1] = i
            else:
                l = lookup[c]
                l[l[-1]] = i
                l[i] = len(s)
                l[-1] = i
            
        pprint(lookup)
            
        # We trying forming a substring from each index `i` in `s`,
        # using the lookup table to exit once we hit a repeated character.
        longest_substr_len = 0
        longest_substr_len_from_i = 0
        for i,c in enumerate(s):
            idx_of_next_repeating_char = lookup[c][i]
            j = i + 1
            while j < idx_of_next_repeating_char:
                idx_of_next_repeating_char = min(idx_of_next_repeating_char, lookup[s[j]][j])
                j += 1
            
            longest_substr_len_from_i = j - i
            if longest_substr_len_from_i > longest_substr_len:
                longest_substr_len = longest_substr_len_from_i

        return longest_substr_len


#print(Solution().lengthOfLongestSubstring("abab"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))