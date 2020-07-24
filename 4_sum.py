from typing import List

class Solution:


    # See 3_sum to understand the solution to this. Basically, the key insight
    # is that the quickest way to find a sum within a list of numbers is to 
    # start from both ends and work towards the middle. 
    # Here, do standard iteration from left-to-right variables a/b.
    # We then determine what sum we'd need to find using c/d and run
    # the algo described above to see if the sum exists.
    # Then finally, each time we iterate an index we skip over duplicates. Pretty standard.

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        combos = []
        a = 0
        while a < len(nums) - 3:
            b = a + 1
            while b < len(nums) - 2:
                search_sum = (target - (nums[a] + nums[b]))
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    search_sum_candidate = nums[c] + nums[d]
                    if search_sum_candidate > search_sum:
                        # iterate, skipping duplicates
                        d -= 1
                        while d >= 0 and nums[d] == nums[d + 1]:
                            d -= 1
                    elif search_sum_candidate < search_sum:
                        # iterate, skipping duplicates.
                        c += 1
                        while c < len(nums) and nums[c] == nums[c - 1]:
                            c += 1
                    else: # they equal! Woot
                        combos.append([nums[a], nums[b], nums[c], nums[d]])
                        # iterate, skipping duplicates
                        d -= 1
                        while d >= 0 and nums[d] == nums[d + 1]:
                            d -= 1
                        c += 1
                        while c < len(nums) and nums[c] == nums[c - 1]:
                            c += 1
                # iterate, skipping duplicates
                b += 1
                while b < len(nums) and nums[b] == nums[b - 1]:
                    b += 1
            # iterate, skipping duplicates
            a += 1
            while a < len(nums) and nums[a] == nums[a - 1]:
                a += 1
                        
        return combos


#print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
#print(Solution().fourSum([0, 0, 0, 0], 1))
#print(Solution().fourSum([-3,-1,0,2,4,5], 2))
print(Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0))

print(Solution().fourSum([0,2,2,2,10,-3,-9,2,-10,-4,-9,-2,2,8,7], 6))

