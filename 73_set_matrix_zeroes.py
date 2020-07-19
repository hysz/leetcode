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
        '''
        i = 0
        min_i = 0
        j = 0
        min_j = 0

        print("MAtrix is %dx%d"%(len(matrix), len(matrix[0])))
        

        # First move the rows up
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j] == 0:
                    # swap each cell of current row with that in `min_i`,
                    # storing the current row index in each cell of the current row
                    for k in range(0, len(matrix[0])):
                        matrix[i][k] = matrix[min_i][k]

                        if matrix[min_i][k] != 0:
                            matrix[min_i][k] = i if i > 0 else -1
                        
                    min_i += 1

                    # Hit up the next row
                    break
                j += 1
            i += 1

        # Next move the columns over
        i = 0
        j = 0
        while i < len(matrix):
            print("i: ", i)
            j = min_j
            while j < len(matrix[0]):
                print("j: ", j)
                if matrix[i][j] == 0:
                    print("FOUND AT (%d, %d)"%(i,j))

                    # swap each cell of current column with that in `min_j`,
                    # storing the current row index in each cell of the current row
                    for k in range(min_i, len(matrix)):
                        matrix[k][j] = matrix[k][min_j]
                        matrix[k][min_j] = j

                    min_j += 1
                j += 1
            i += 1



        

        print("min: (%d, %d)"%(min_i, min_j))

'''
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
'''
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print(matrix)
Solution().setZeroes(matrix)
pprint(matrix)
