import collections
from typing import List

Point = collections.namedtuple('Point', ['x','y'])

class Solution:
    
    def getArea(p1: Point, p2: Point) -> int:
        return (p2.x - p1.x) * min(p1.y, p2.y)
    
    def cannotBeatMaxArea(max_area: int, p1: Point, x2: int) -> int:
        # We've passed our best remaining case when:
        #    getArea(p1, Point(x2, p1.y)) <= max_area
        #    => (p2.x - p1.x) * p1.y <= max_area
        return (x2 - p1.x) * p1.y <= max_area
    
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        
        for x1,y1 in enumerate(heights):
            p1 = Point(x1, y1)
            x2 = len(heights) - 1
            for x2 in range(len(heights) - 1, x1, -1):
                if Solution.cannotBeatMaxArea(max_area, p1, x2):
                    break
                    
                volume = Solution.getArea(p1, Point(x2, heights[x2]))
                if volume > max_area:
                    max_area = volume
        
        return max_area
        
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))