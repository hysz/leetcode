from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        combos = []

        for a in range(0, len(nums) - 3):
            for b in range(a + 1, len(nums) - 2):
                search_sum = (target - (nums[a] + nums[b]))
                c = b + 1
                d = len(nums) - 1
                while c != d:
                    search_sum_candidate = nums[c] + nums[d]
                    if search_sum_candidate > search_sum:
                        d -= 1
                    elif search_sum_candidate < search_sum:
                        c += 1
                    else: # they equal! Woot
                        combos.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
        return combos


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
#print(Solution().fourSum([0, 0, 0, 0], 1))
#print(Solution().fourSum([-3,-1,0,2,4,5], 2))


