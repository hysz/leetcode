class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        mapping = {}
        reverse_mapping = {}
        for i in range(0, len(words)):
            if not pattern[i] in mapping:
                if not words[i] in reverse_mapping:
                    mapping[pattern[i]] = words[i]
                    reverse_mapping[words[i]] = mapping[pattern[i]]
                else:
                    return False
            elif mapping[pattern[i]] != words[i]:
                return False
            
        return True
        