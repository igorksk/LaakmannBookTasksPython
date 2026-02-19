"""Chapter 1 - Set Matrix Zeroes

Problem: If an element in an MxN matrix is 0, set its entire row and
column to 0. This module implements a two-pass approach identifying
rows and columns to zero out.
"""

def set_zeros(matrix):
    if not matrix or not matrix[0]:
        return

    rows, cols = len(matrix), len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    # First pass: find all zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Second pass: set rows to zero
    for i in range(rows):
        if i in zero_rows:
            for j in range(cols):
                matrix[i][j] = 0

    # Third pass: set columns to zero
    for j in range(cols):
        if j in zero_cols:
            for i in range(rows):
                matrix[i][j] = 0


input_matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]
print("Original matrix:")
for row in input_matrix:
    print(row)
set_zeros(input_matrix)
print("Matrix after setting zeros:")
for row in input_matrix:
    print(row)
    