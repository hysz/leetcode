from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        # seed
        best_sum = nums[0] + nums[1] + nums[2]
        best_diff = abs(best_sum - target)
        
        # find best
        for i in range(0, len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                # avoid duplicates
                continue
                
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum_ijk = nums[i] + nums[j] + nums[k]
                diff = abs(sum_ijk - target)
                if diff < best_diff:
                    best_sum = sum_ijk
                    best_diff = diff
                    if diff == 0:
                        return sum_ijk
                
                # move j/i accordingly
                if sum_ijk < target:
                    j += 1
                elif sum_ijk > target:
                    k -= 1
                else:
                    j += 1
                    k -= 1
        return best_sum

print(Solution().threeSumClosest([0,1,2], 3))