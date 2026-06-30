from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # 1. 判断第一行本来是否有 0
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        # 2. 判断第一列本来是否有 0
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
                break

        # 3. 用第一行和第一列做标记
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # 4. 根据第一列的标记，把对应行变成 0
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0

        # 5. 根据第一行的标记，把对应列变成 0
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0

        # 6. 如果第一行原本有 0，把第一行全部变成 0
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # 7. 如果第一列原本有 0，把第一列全部变成 0
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
        