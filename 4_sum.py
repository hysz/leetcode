from typing import List

class Solution:
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
                        d -= 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif search_sum_candidate < search_sum:
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                    else: # they equal! Woot
                        '''
                        print([a, b, c, d])
                        print([nums[a], nums[b], nums[c], nums[d]])
                        print("--")
                        '''
                        combos.append([nums[a], nums[b], nums[c], nums[d]])
                        # iterate, skipping duplicates
                        d -= 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                        c += 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                b += 1
                while b < c and nums[b] == nums[b - 1]:
                    b += 1
            a += 1
            while a < b and nums[a] == nums[a - 1]:
                a += 1
                        
        return combos


#print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
#print(Solution().fourSum([0, 0, 0, 0], 1))
#print(Solution().fourSum([-3,-1,0,2,4,5], 2))
print(Solution().fourSum([-3,-2,-1,0,0,1,2,3], 0))

