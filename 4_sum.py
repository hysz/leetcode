from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        a = 0
        b = 1
        c = len(nums) - 2
        d = len(nums) - 1

        combos = []

        while a < b and b < c and c < d:
            print("[%d,%d,%d,%d]"%(a,b,c,d))
            total = nums[a] + nums[b] + nums[c] + nums[d]
            if total < target:
                if (a < b - 1 and (target - total) >= (nums[b] - nums[a])) or b == c - 1:
                    a += 1
                else:
                    b += 1
            elif total > target:
                if (d > c + 1 and (total - target) >= (nums[d] - nums[c])) or b == c - 1:
                    d -= 1
                else:
                    c -= 1
            else:
                combos.append([nums[a],nums[b],nums[c],nums[d]])
                if b != c - 1:
                    b += 1
                elif a < b - 1:
                    a += 1
                elif d > c + 1:
                    d -= 1
                else:
                     break

        return combos

            #if b == (c - 1) and a == (b - 1) and c == (d - 1):
            #    break


#print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
#print(Solution().fourSum([0, 0, 0, 0], 1))
print(Solution().fourSum([-3,-1,0,2,4,5], 2))


