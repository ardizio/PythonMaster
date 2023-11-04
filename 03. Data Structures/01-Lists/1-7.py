def rotate_image(matrix):
    if not matrix:
        return

    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

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

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_image(matrix)

for row in matrix:
    print(row)
