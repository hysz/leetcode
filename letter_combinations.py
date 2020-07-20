from typing import List

class Solution:
    def getLettersByNumber(digit: int) -> str:#List[str]:
        char_range = range(0, 3) if (digit != 7 and digit != 9) else range(0, 4)
        offset = 0 if digit <= 7 else 1
        return [chr(ord("a") + offset + (digit - 2) * 3 + i) for i in char_range]


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        combinations = []
        for char in Solution.getLettersByNumber(int(digits[0:1])):
            char_combinations = self.letterCombinations(digits[1:])
            if not char_combinations:
                combinations.append(char)
                continue

            for combo in char_combinations:
                combinations.append(char + combo)

        return combinations


'''      
print(Solution.getLettersByNumber(2))
print(Solution.getLettersByNumber(3))
print(Solution.getLettersByNumber(4))
print(Solution.getLettersByNumber(5))
print(Solution.getLettersByNumber(6))
print(Solution.getLettersByNumber(7))
print(Solution.getLettersByNumber(8))
print(Solution.getLettersByNumber(9))
'''
#print(Solution().letterCombinations("23"))
print(Solution().letterCombinations("234"))
