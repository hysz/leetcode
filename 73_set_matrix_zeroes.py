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
        
        while i < len(matrix):
            print("i: ", i)
            j = 0
            while j < len(matrix[0]):
                print("j: ", j)
                if matrix[i][j] == 0:
                    print("Yo")
                    # swap each cell of current row with that in `min_i`,
                    # storing the current row index in each cell of the current row
                    for k in range(min_j, len(matrix[0])):
                        matrix[i][k] = matrix[min_i][k]
                        matrix[min_i][k] = j
                        
                    min_i += 1
                    
                    # swap each cell of current column with that in `min_j`,
                    # storing the current row index in each cell of the current row
                    for k in range(min_i, len(matrix)):
                        matrix[k][j] = matrix[k][min_j]
                        matrix[k][min_j] = i
                        
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
Solution().setZeroes(matrix)
pprint(matrix)
