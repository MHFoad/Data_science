def extract_and_transform_diagonals (matrix):
    n=len(matrix) # size of the square matrix

    main_daigonal= [2*(matrix[i][i]) if matrix[i][i]%2 ==0 else matrix[i][i] for i in range (n)] # in diagonal matrix row == column means i==j

    anti_daigonal=[matrix[i][n-i-1]/2 if matrix[i][n-i-1] %2 !=0 else matrix[i][n-i-1] for i in range (n)] #anti diagonal elements of a square matrix can be found through matrix[i][n-i-1]

    return (main_daigonal , anti_daigonal)




matrix = [
    [1, 2, 3, 5],
    [4, 5, 6, 8],
    [7, 8, 9, 10],
    [4, 6, 9, 12]
]

result = extract_and_transform_diagonals(matrix)
print (result)