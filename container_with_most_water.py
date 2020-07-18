from typing import List
import math

class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        max_x2 = len(heights) - 1
        for x1,y1 in enumerate(heights):
            # no area when height is zero
            if y1 == 0:
                continue

            # first check to see if we can even beat max area
            if (max_x2 - x1) * y1 <= max_area:
                continue

            # lets try to beat the max area
            min_delta_x_to_beat = math.ceil(max_area / y1)
            for x2 in range(max_x2, x1 + min_delta_x_to_beat - 1, -1):
                area = (x2 - x1) * min(y1, heights[x2])
                if area > max_area:
                    max_area = area
                    # check if any future iteration could do better
                    if (x2 - 1 - x1) * y1 <= max_area:
                        break
                        
        
        return max_area


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1]))
print(Solution().maxArea([]))
print(Solution().maxArea([0]))


print(Solution().maxArea([1,3,2,5,25,24,5]))
