from pprint import pprint

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        grid = [[] for r in range(0,num_rows)]
        
        n = 0
        while n < len(s):
            i = 0
            while i < num_rows and n < len(s):
                grid[i].append(s[n])
                i += 1
                n += 1
            
            i = num_rows - 2
            while i > 0 and n < len(s):
                grid[i].append(s[n])
                i -= 1
                n += 1
        
        pprint(grid)
        output = "".join([c for row in grid for c in row])
        return output
        

#pprint(Solution().convert("PAYPALISHIRING", 3))
#pprint(Solution().convert("PAYPALISHIRING", 4))


pprint(Solution().convert("GREG", 2))