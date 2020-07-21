from typing import List
from collections import defaultdict

class Solution:
    exists = None
    
    def getCombinations(self, nums: List[int], size: int) -> List[int]:
        if size == 0:
            return []
        elif size == 1:
            return [[n] for n in nums]
        
        exists = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
        combos = []
        for i,n in enumerate(nums):
            n_combos = self.getCombinations(nums[(i+1):], size - 1)
            
            # Aggregate if we're not at the top-level of recursion (inferred by size=3)
            if size != 3:
                combos += [[n] + n_combo for n_combo in n_combos]
                continue
            
            # This is where we aggregate the combos with 3 elements
            for n_combo in n_combos:
                # Check if this combo equals zero.
                n2 = n_combo[0]
                n3 = n_combo[1]
                if n + n2 != -n3:
                    continue
                
                # Check if we've already recorded this combo.
                if self.exists[n][n2][n3]:
                    continue
                self.exists[n][n2][n3] = True

                # Woot, we found a unique combo that sums to zero!
                combos.append([n,n2,n3])

        return combos
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.exists = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
        return self.getCombinations(sorted(nums), 3)

#print(Solution.getCombinations([1,2,3,4], 2))

print(Solution().threeSum([-1,0,1]))

#print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
#print(Solution().threeSum([0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]))
#print(Solution().threeSum([7,5,-8,-6,-13,7,10,1,1,-4,-14,0,-1,-10,1,-13,-4,6,-11,8,-6,0,0,-5,0,11,-9,8,2,-6,4,-14,6,4,-5,0,-12,12,-13,5,-6,10,-10,0,7,-2,-5,-12,12,-9,12,-9,6,-11,1,14,8,-1,7,-13,8,-11,-11,0,0,-1,-15,3,-11,9,-7,-10,4,-2,5,-4,12,7,-8,9,14,-11,7,5,-15,-15,-4,0,0,-11,3,-15,-15,7,0,0,13,-7,-12,9,9,-3,14,-1,2,5,2,-9,-3,1,7,-12,-3,-1,1,-2,0,12,5,7,8,-7,7,8,7,-15]))