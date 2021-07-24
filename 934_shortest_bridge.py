import pprint
pp = pprint.PrettyPrinter(indent=2)
from typing import List
import sys

class Solution:
    
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # pp.pprint(grid)
        islands = [[], []]
        idx = 0

        # Fetch our islands
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] <= 0:
                    continue
                
                squares = [[i,j]]
                while len(squares) > 0:
                    square = squares.pop(0)
                    if grid[square[0]][square[1]] != 1:
                        continue
                    
                    islands[idx].append([square[0], square[1]])
                    grid[square[0]][square[1]] = -1 * (idx + 1)

                    if square[0] > 0:
                        squares.append([square[0] - 1, square[1]])
                    if square[1] > 0:
                        squares.append([square[0], square[1] - 1])
                    if square[0] < len(grid) - 1:
                        squares.append([square[0] + 1, square[1]])
                    if square[1] < len(grid[i]) - 1:
                        squares.append([square[0], square[1] + 1])

                idx += 1  
            
        # pp.pprint(grid)
        # pp.pprint(islands)

        # Now that we have our islands we simply find the min distance between two points in each set.
        minDist = sys.maxsize
        for a in islands[0]:
            for b in islands[1]:
                dist = abs(a[0] - b[0]) + abs(a[1] - b[1]) - 1
                if dist < minDist:
                    minDist = dist
                    if minDist == 1:
                        return 1
        return minDist            
                 

#print(Solution().shortestBridge([[0,1],[1,0]]))
#print(Solution().shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
#print(Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))