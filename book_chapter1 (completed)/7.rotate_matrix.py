def matrix_rotate(matrix):
    """
    Rotate a square matrix 90 degrees clockwise in place.
    
    :param matrix: List of lists representing the square matrix
    :return: None, the matrix is modified in place
    """
    n = len(matrix)
    for layer in range(n // 2): 
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            # Save the top element
            top = matrix[first][i]
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            # Move top to right
            matrix[i][last] = top    
    return matrix

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    
print("Original matrix:")
for row in input_matrix:
    print(row)
    
matrix_rotate(input_matrix)
    
print("Rotated matrix:")
for row in input_matrix:
    print(row)

