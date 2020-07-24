from typing import List

class Solution:
    def permute(current: List[int], entries: List[int], k: List[int]) -> List[int]:
        if not entries:
            k[0] -= 1
            if (k[0] == 0):
                return current
            else:
                return None
                
        for i,entry in enumerate(entries):
            maybe_kth_permutation = Solution.permute(current + [entry], entries[:i] + entries[i + 1:], k)
            if maybe_kth_permutation:
                return maybe_kth_permutation
    
    def getPermutation(self, n: int, k: int) -> str:
        k_as_object = [k]
        kth_permutation = Solution.permute([], [a for a in range(1, n + 1)], k_as_object)
        return str("".join([str(elem) for elem in kth_permutation]))

print(Solution().getPermutation(3, 3))