def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [max[::-1] for max in matrix]


print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))
