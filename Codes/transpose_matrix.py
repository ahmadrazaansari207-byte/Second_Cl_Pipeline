def transpose_matrix(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    for j in range(cols):
        row = []

        for i in range(rows):
            row.append(matrix[i][j])

        result.append(row)

    return result


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    matrix = []

    for i in range(rows):
        row = list(map(int, input("Enter row elements separated by spaces: ").split()))
        matrix.append(row)

    print("Transposed matrix:")

    for row in transpose_matrix(matrix):
        print(row)



#c:\Raza\Second_Cl_Pipeline\Codes\transpose_matrix.py