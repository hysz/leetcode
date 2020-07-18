from pprint import pprint

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)

        '''
        We construct a lookup table that allows you to query for next occurence of a character.
        Ex for string "abab"
            {
                "a:
                {
                    0: 2,
                    2: -1,
                    -1: 2   // Used to lookup furthest occurence
                },
                "b":
                {
                    1: 3,
                    3: -1
                }
            }
        '''

        # construct lookup
        lookup = {}
        for i,c in enumerate(s):
            if not c in lookup:
                lookup[c] = {}
                l = lookup[c]
                l[i] = -1
                l[-1] = i
            else:
                l = lookup[c]
                l[l[-1]] = i
                l[i] = -1
                l[-1] = i
            
        pprint(lookup)
            
        # We now iterate through `str` a second time.
        # The longest substring not containing the current
        # character will be the distance to the next entry
        # in the lookup table for that char. If there is no
        # more entries than it's the end of the string.
        longest_substr_len = 0
        for i,c in enumerate(s):
            longest_substr_len_from_i = 0
            if not lookup[c]:
                longest_substr_len_from_i = len(s) - i
            else:
                longest_substr_len_from_i = lookup[c][0] - i
                # remove from the lookup table, so that
                # whenever you do lookup[c][0] it'll have
                # the next occurence of c.
                del lookup[c][0]
            
            if longest_substr_len_from_i > longest_substr_len:
                longest_substr_len = longest_substr_len_from_i

            print("From `%d` we have %d"%(i,longest_substr_len_from_i))

        return longest_substr_len


print(Solution().lengthOfLongestSubstring("abab"))
#print(Solution().lengthOfLongestSubstring("abcabcbb"))