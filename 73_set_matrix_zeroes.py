from typing import List
from pprint import pprint

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        '''
        I'll be honest ... This took me some time to figure out.
        Not sure how amped I am about this problem. Seems kinda .. dubious.

        This is how I did it:
        The key insight is that you need to use the space you've already traversed to hold state for rows/columns
        that should be zeroed out.

        Algo:
        1. Scan over all rows. If you come across a "0" in any of the rows then this row will
           be swapped with the row at `min_i`. Since all values in the current row will be zeroed
           out, we record in each cell where this row is located so that we can swap it back later on.
           It would be nice to just store `i` but this doesn't work. We need a way to retain which cells
           hold a zero for when we process the columns later on. Since zero is a special value, I opted to
           avoid that value altogether and store either (i+1) or -(i+1); the negative value signals that this
           cell was a zero. This will come in handy when processing the columns.

        2. Scan over all columns. If we come across a cell with zero (or a negative value in a zeroed row from #1), then
           this column will be swapped with the column at `min_j`. We do not swap cells in rows that are <min_i (ie, rows that will be zeroed out).
           This is because we don't want to lose the state from that row (which row it should be swapped back for later on). Additionally,
           to avoid processing this same column again, we un-negate all cells in rows less than min_i.

        3. Move columns back into place, zeroeing out fields. This part is easy, basically just the reverse of #2. Unwind each swapped column;
           swap back the column and zero each cell.

        4. Move rowes back into place, zeroeing out fields. This part is easy, basically just the reverse of #1. Unwind each swapped row;
           swap back the row and zero each cell.


        Example:
        Input:
        [
            [0,1,2,0],
            [3,4,5,0],
            [6,7,8,9],
            [1,3,1,0]
        ]

        Step 1:
        [
            [-1, 1, 1, -1]
            [2, 2, 2, -2]
            [4, 4, 4, -4]
            [6, 7, 8, 9]
        ]
        min_i = 3 (ie, all rows up to i=3 will be swapped and zeroed later on)

        Step 2:
        [
            [1, 1, 1, 1]
            [2, 2, 2, 2]
            [4, 4, 4, 4]
            [0, 3, 8, 7]
        ]
        min_j = 2

        Step 3:
        [
            [1, 1, 1, 1]
            [2, 2, 2, 2]
            [4, 4, 4, 4]
            [0, 7, 8, 0]
        ]

        Step 4:
        [
            [0, 0, 0, 0]
            [0, 0, 0, 0]
            [0, 7, 8, 0]
            [0, 0, 0, 0]
        ]
        '''
        
        # THIS IS OUR STATE -- SUPER O(1)
        i = 0
        min_i = 0
        j = 0
        min_j = 0

        # STEP 1 - PROCESS ROWS.
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j] == 0:
                    # swap each cell of current row with that in `min_i`,
                    # storing the current row index in each cell of the current row
                    for k in range(0, len(matrix[0])):
                        is_zero = matrix[i][k] == 0
                        matrix[i][k] = matrix[min_i][k]
                        
                        # store the (row + 1), unless the cell is zero and then store -(row + 1)
                        matrix[min_i][k] = i + 1
                        if is_zero:
                            matrix[min_i][k] *= -1

                    min_i += 1

                    # Hit up the next row
                    break
                j += 1
            i += 1
        
        # STEP 2 - PROCESS COLUMNS.
        i = 0
        j = 0
        while i < len(matrix):

            #print("i: ", i)
            j = min_j
            while j < len(matrix[0]):
                #print("j: ", j)
                if matrix[i][j] == 0 or (i < min_i and matrix[i][j] < 0):
                    
                    #print("FOUND AT (%d, %d)"%(i,j))


                    # mark that we got this column so it does not get processed again.
                    # we do this simply by ensuring all cells are positive.
                    for k in range(0, min_i):
                        matrix[k][j] = abs(matrix[k][j])

                    # swap each cell of current column with that in `min_j`,
                    # storing the current row index in each cell of the current row
                    for k in range(0, len(matrix)):
                        matrix[k][j] = matrix[k][min_j]
                        # We don't want to overwrite cells that belong to rows that were zeroed.
                        if k >= min_i:
                            matrix[k][min_j] = j

                    min_j += 1
                j += 1
            i += 1

        # STEP 3 - Move columns back into place, zeroeing where necessary.
        if min_i < len(matrix):
            j = min_j - 1
            while j >= 0:
                col = matrix[min_i][j]
                for i in range(min_i, len(matrix)):
                    matrix[i][j] = matrix[i][col]
                    matrix[i][col] = 0
                j -= 1
        
        # STEP 4 - Move rows back into place, zeroeing where necessary.
        i = min_i - 1
        while i >= 0:
            row = abs(matrix[i][0]) - 1
            for j in range(0, len(matrix[0])):
                matrix[i][j] = matrix[row][j]
                matrix[row][j] = 0
            i -= 1

def print_matrix(matrix):
    for i in range(0, len(matrix)):
        pprint(matrix[i])
    print("-----")

'''
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]


matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,0]
]


'''
'''
matrix = [
    [0,0,0,5],
    [4,3,1,4],
    [0,1,1,4],
    [1,2,1,3],
    [0,0,1,1]
]
matrix = [[0]]

matrix = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
'''

#matrix = [[8,3,6,9,7,8,0,6],[0,3,7,0,0,4,3,8],[5,3,6,7,1,6,2,6],[8,7,2,5,0,6,4,0],[0,2,9,9,3,9,7,3]]

#matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

matrix = [
  [0,1,2,0],
  [3,4,5,0],
  [6,7,8,9],
  [1,3,1,0]
]

print_matrix(matrix)
Solution().setZeroes(matrix)
print_matrix(matrix)

print("-- EXPECTED --")
#print_matrix([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,3,6,0,0,6,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]])
