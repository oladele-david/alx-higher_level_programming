def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Compute the square value for each element in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
