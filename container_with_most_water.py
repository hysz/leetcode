import collections
from typing import List
import math

Point = collections.namedtuple('Point', ['x','y'])

class Solution:
    
    def getArea(p1: Point, p2: Point) -> int:
        return (p2.x - p1.x) * min(p1.y, p2.y)
    
    def cannotBeatMaxArea(max_area: int, p1: Point, x2: int) -> int:
        # We've passed our best remaining case when:
        #    getArea(p1, Point(x2, p1.y)) <= max_area
        #    => (p2.x - p1.x) * p1.y <= max_area
        return 
    
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        
        max_x2 = len(heights) - 1
        for x1,y1 in enumerate(heights):
            p1 = Point(x1, y1)
            x2 = len(heights) - 1

            # no area when height is zero
            if y1 == 0:
                continue

            # first check to see if we cannot beat max area
            min_delta_x_to_beat = math.ceil(max_area / y1)
            if max_x2 - x1 < min_delta_x_to_beat:
                print("break1")
                continue

            for x2 in range(max_x2, x1 + min_delta_x_to_beat - 1, -1):
                if (x2 - p1.x) * p1.y <= max_area:
                    print("Break2")
                    break
                    
                volume = Solution.getArea(p1, Point(x2, heights[x2]))
                if volume > max_area:
                    print("Max area: [%d..%d] = %d"%(x1, x2, volume))
                    max_area = volume
        
        return max_area

'''
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
print(Solution().maxArea([1]))
print(Solution().maxArea([]))
print(Solution().maxArea([0]))
'''

print(Solution().maxArea([1,3,2,5,25,24,5]))
