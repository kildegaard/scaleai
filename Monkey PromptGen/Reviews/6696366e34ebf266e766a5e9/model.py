def rotate_matrix(matrix, r):
    """Rotates a 2D matrix anti-clockwise 'r' times.

    Args:
        matrix: The input 2D matrix.
        r: The number of rotations.

    Returns:
        The rotated matrix.
    """

    m, n = len(matrix), len(matrix[0])
    min_dim = min(m, n) // 2  # Number of layers to rotate

    for _ in range(r):
        for layer in range(min_dim):
            top = left = layer
            bottom = m - layer - 1
            right = n - layer - 1

            # Store the top-left corner element
            temp = matrix[top][left]

            # Move elements from left to top
            for i in range(left + 1, right + 1):
                matrix[top][i - 1] = matrix[top][i]

            # Move elements from bottom to left
            for i in range(top + 1, bottom + 1):
                matrix[i - 1][left] = matrix[i][left]

            # Move elements from right to bottom
            for i in range(bottom - 1, top - 1, -1):
                matrix[bottom][i + 1] = matrix[bottom][i]

            # Move the stored element to the right
            for i in range(right - 1, left - 1, -1):
                matrix[i + 1][right] = matrix[i][right]

            matrix[top + 1][right] = temp

    return matrix


# Example usage
start = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

result = rotate_matrix(start, 2)
for row in result:
    print(row)
