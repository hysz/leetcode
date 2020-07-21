from typing import List
from collections import defaultdict

class Solution:
   
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        combos = []
        exists = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
        for i in range(0, len(nums)):
            ni = nums[i]
            if i > 0 and ni == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                nj = nums[j]
                if j > i+1 and nj == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    nk = nums[k]
                    # Check if this combo equals zero.
                    if ni + nj != -nk:
                        continue

                    if k > j+1 and nums[k] == nums[k-1]:
                        continue

                    # Woot, we found a unique combo that sums to zero!
                    combos.append([ni,nj,nk])

        return combos

#print(Solution.getCombinations([1,2,3,4], 2))

#print(Solution().threeSum([-1,0,1]))

#print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
#print(Solution().threeSum([0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]))
#print(Solution().threeSum([7,5,-8,-6,-13,7,10,1,1,-4,-14,0,-1,-10,1,-13,-4,6,-11,8,-6,0,0,-5,0,11,-9,8,2,-6,4,-14,6,4,-5,0,-12,12,-13,5,-6,10,-10,0,7,-2,-5,-12,12,-9,12,-9,6,-11,1,14,8,-1,7,-13,8,-11,-11,0,0,-1,-15,3,-11,9,-7,-10,4,-2,5,-4,12,7,-8,9,14,-11,7,5,-15,-15,-4,0,0,-11,3,-15,-15,7,0,0,13,-7,-12,9,9,-3,14,-1,2,5,2,-9,-3,1,7,-12,-3,-1,1,-2,0,12,5,7,8,-7,7,8,7,-15]))
#print(Solution().threeSum([13,-5,3,3,-1,13,3,1,-9,-4,9,12,6,-9,-6,-12,-8,3,12,14,4,-15,2,-11,4,-12,10,9,-6,-3,-8,14,7,3,2,-8,-7,-10,8,-8,-7,-6,-11,6,-7,-2,9,-8,8,-2,13,-10,-2,0,-14,-13,-4,11,3,-3,-7,3,-4,8,13,13,-15,-9,10,0,-2,-12,1,2,9,1,8,-4,8,-7,9,7,-2,-15,14,0,-13,-13,-12,-2,-1,-11,8,10,12,6,8,4,12,3,11,-12,-2,-3,5,-15,6,-10,-4,-1,-1,-10,13]))
print(Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
#print(len(Solution().threeSum([1,2,3,4,5,6,7,8])))