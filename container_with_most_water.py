from typing import List
import math
import json
from pprint import pprint

class Solution:
    
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        max_x2 = len(heights) - 1
        
        for x1,y1 in enumerate(heights):
            # no area when height is zero
            if y1 == 0:
                continue

            # lets try to beat the max area
            min_x2_to_beat_max_area = x1 + max(1, math.ceil(float(max_area) / float(y1)))
            x2 = max_x2
            while x2 >= min_x2_to_beat_max_area:
                # check if any future iteration could do better
                area = (x2 - x1) * min(y1, heights[x2])
                if area > max_area:
                    max_area = area
                    min_x2_to_beat_max_area = x1 + max(1, math.ceil(float(max_area) / float(y1)))

                x2 -= 1

        return max_area

'''
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1]))
print(Solution().maxArea([]))
print(Solution().maxArea([0]))



print(Solution().maxArea([1,3,2,5,25,24,5]))


'''
print(Solution().maxArea(json.load(open('./ar.json'))))
