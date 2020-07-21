from typing import List

class Solution:

    def gen(s: str) -> List[str]:
        combos = []
        combos.append("(%s)"%(s))
        combos.append("()%s"%(s))
        return combos

    def generate(n: int) -> List[List[str]]:
        if n == 1:
            return [["()"]]

        combos = []
        combos_i = Solution.generate(n-1)
        for combo in combos_i:
            for group_size in range(1, len(combo) + 1):
                i = 0
                while i <= len(combo) - group_size:
                    # Wrap current element
                    wrapped = combo[:i] + ["(%s)"%("".join(combo[i:i + group_size]))] + combo[i + group_size:]
                    if not wrapped in combos:
                        combos.append(wrapped)
                    # Next group size
                    i += group_size
           
            # Wrap no elements
            sequential = ["()"] + combo
            if not sequential in combos:
                combos.append(sequential)
        return combos


    def generateParenthesis(self, n: int) -> List[str]:
        combos = ["".join(combo) for combo in Solution.generate(n)]
        #print(combos)
        return combos


actual = Solution().generateParenthesis(4)
expected = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]

actual_extra = [e for e in actual if not e in expected]
actual_missing = [e for e in expected if not e in actual]

print("Extra:")
print(actual_extra)
print("Missing:")
print(actual_missing)