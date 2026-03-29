class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroRows = set()
        zeroColumns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroRows.add(i)
                    zeroColumns.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i not in zeroRows and j not in zeroColumns:
                    pass
                else:
                    matrix[i][j]=0
        
        
        